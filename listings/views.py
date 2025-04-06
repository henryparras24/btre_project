from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from datetime import datetime

# Static listings data
LISTINGS = [
    {
        'id': 1,
        'title': 'Beautiful Family Home',
        'address': '123 Main St',
        'city': 'Boston',
        'state': 'MA',
        'zipcode': '02108',
        'description': 'Gorgeous family home in a quiet neighborhood',
        'price': 750000,
        'bedrooms': 4,
        'bathrooms': 3,
        'garage': 2,
        'sqft': 2500,
        'lot_size': 0.5,
        'is_published': True,
        'list_date': datetime(2024, 3, 1),
        'photo_main': 'img/homes/home1.jpg',
        'photo_1': 'img/homes/home1_1.jpg',
        'photo_2': 'img/homes/home1_2.jpg',
        'photo_3': '',
        'photo_4': '',
        'photo_5': '',
        'photo_6': '',
        'realtor': {
            'id': 1,
            'name': 'John Doe',
            'photo': 'img/realtors/agent.jpg',
            'description': 'Top agent with over 10 years of experience',
            'phone': '555-555-5555',
            'email': 'john@example.com',
            'is_mvp': True
        }
    },
    {
        'id': 2,
        'title': 'Downtown Condo',
        'address': '456 Park Ave',
        'city': 'Boston',
        'state': 'MA',
        'zipcode': '02116',
        'description': 'Modern condo in the heart of downtown',
        'price': 500000,
        'bedrooms': 2,
        'bathrooms': 2,
        'garage': 1,
        'sqft': 1200,
        'lot_size': 0.0,
        'is_published': True,
        'list_date': datetime(2024, 3, 15),
        'photo_main': 'img/homes/home2.jpg',
        'photo_1': '',
        'photo_2': '',
        'photo_3': '',
        'photo_4': '',
        'photo_5': '',
        'photo_6': '',
        'realtor': {
            'id': 2,
            'name': 'Jane Smith',
            'photo': 'img/realtors/hsquare.png',
            'description': 'Specializing in luxury properties',
            'phone': '555-555-5556',
            'email': 'jane@example.com',
            'is_mvp': False
        }
    },
    # Add more listings as needed
]

def index(request):
    # Filter published listings and sort by date
    listings = [listing for listing in LISTINGS if listing['is_published']]
    listings.sort(key=lambda x: x['list_date'], reverse=True)
    
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    
    return render(request, 'listings/listings.html', context)
    
def listing(request, listing_id):
    # Find listing by id
    listing = next((item for item in LISTINGS if item['id'] == listing_id), None)
    
    if listing is None:
        from django.http import Http404
        raise Http404("Listing does not exist")

    context = {
        'listing': listing 
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    # Start with all published listings
    queryset_list = [listing for listing in LISTINGS if listing['is_published']]
    
    # Keywords
    if 'keywords' in request.GET and request.GET['keywords']:
        keywords = request.GET['keywords'].lower()
        queryset_list = [listing for listing in queryset_list 
                          if keywords in listing['description'].lower()]

    # City
    if 'city' in request.GET and request.GET['city']:
        city = request.GET['city'].lower()
        queryset_list = [listing for listing in queryset_list 
                          if listing['city'].lower() == city]

    # State
    if 'state' in request.GET and request.GET['state']:
        state = request.GET['state']
        queryset_list = [listing for listing in queryset_list 
                          if listing['state'] == state]

    # Bedrooms
    if 'bedrooms' in request.GET and request.GET['bedrooms']:
        bedrooms = int(request.GET['bedrooms'])
        queryset_list = [listing for listing in queryset_list 
                          if listing['bedrooms'] <= bedrooms]

    # Price
    if 'price' in request.GET and request.GET['price']:
        price = int(request.GET['price'])
        queryset_list = [listing for listing in queryset_list 
                          if listing['price'] <= price]

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)









# from django.shortcuts import get_object_or_404, render
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from .choices import price_choices, bedroom_choices, state_choices

# from .models import Listing

# def index(request):
#     listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
#     paginator = Paginator(listings, 6)
#     page = request.GET.get('page')
#     paged_listings = paginator.get_page(page)

#     context = {
#         'listings': paged_listings
#     }
    
#     return render(request, 'listings/listings.html', context)
    

# def listing(request, listing_id):
#     listing = get_object_or_404(Listing, pk=listing_id)

#     context = {
#         'listing': listing 
#     }

#     return render(request, 'listings/listing.html', context)

# def search(request):
#     queryset_list = Listing.objects.order_by('-list_date')

#     # Keywords
#     if 'keywords' in request.GET:
#         keywords = request.GET['keywords']
#         if keywords: 
#             queryset_list = queryset_list.filter(description__icontains=keywords)

#     #City
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city: 
#             queryset_list = queryset_list.filter(city__iexact=city)     

#     #State
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state: 
#             queryset_list = queryset_list.filter(state__iexact=state) 

#     #Bedrooms
#     if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms: 
#             queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) 

#     #Price
#     if 'price' in request.GET:
#         price = request.GET['price']
#         if price: 
#             queryset_list = queryset_list.filter(price__lte=price)               

#     context = {
#         'state_choices': state_choices,
#         'bedroom_choices': bedroom_choices,
#         'price_choices': price_choices,
#         'listings': queryset_list,
#         'values': request.GET
#     }

#     return render(request, 'listings/search.html', context)
