from django.core.management.base import BaseCommand
from realtors.models import Realtor
from listings.models import Listing
from datetime import datetime

class Command(BaseCommand):
    help = 'Adds sample realtors and listings'

    def handle(self, *args, **options):
        # Clear existing data
        Listing.objects.all().delete()
        Realtor.objects.all().delete()
        
        # Create realtors
        realtor1 = Realtor.objects.create(
            name='John Doe',
            photo='photos/realtors/agent.jpg',
            description='Top agent with over 10 years of experience',
            phone='555-555-5555',
            email='john@example.com',
            is_mvp=True
        )
        
        realtor2 = Realtor.objects.create(
            name='Jane Smith',
            photo='photos/realtors/agent2.jpg',
            description='Specializing in luxury properties',
            phone='555-555-5556',
            email='jane@example.com',
            is_mvp=False
        )
        
        # Create listings
        Listing.objects.create(
            realtor=realtor1,
            title='Beautiful Family Home',
            address='123 Main St',
            city='Boston',
            state='MA',
            zipcode='02108',
            description='Gorgeous family home in a quiet neighborhood',
            price=750000,
            bedrooms=4,
            bathrooms=3,
            garage=2,
            sqft=2500,
            lot_size=0.5,
            is_published=True,
            list_date=datetime.now(),
            photo_main='photos/homes/home1.jpg',
            photo_1='photos/homes/home1_1.jpg',
            photo_2='photos/homes/home1_2.jpg'
        )
        
        Listing.objects.create(
            realtor=realtor2,
            title='Downtown Condo',
            address='456 Park Ave',
            city='Boston',
            state='MA',
            zipcode='02116',
            description='Modern condo in the heart of downtown',
            price=500000,
            bedrooms=2,
            bathrooms=2,
            garage=1,
            sqft=1200,
            lot_size=0.0,
            is_published=True,
            list_date=datetime.now(),
            photo_main='photos/homes/home2.jpg'
        )
        
        self.stdout.write(self.style.SUCCESS('Successfully created sample data'))