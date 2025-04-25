from django.core.management.base import BaseCommand
from booking.models import Show
from datetime import date, time

class Command(BaseCommand):
    help = 'Populate the database with sample shows'

    def handle(self, *args, **kwargs):
        Show.objects.all().delete()  # Clear existing shows

        sample_shows = [
            {
                'title': 'Concert Night',
                'description': 'An amazing night of live music.',
                'date': date(2025, 5, 1),
                'time': time(19, 0),
                'total_seats': 100,
                'available_seats': 100,
            },
            {
                'title': 'Comedy Show',
                'description': 'Laugh out loud with the best comedians.',
                'date': date(2025, 5, 3),
                'time': time(20, 0),
                'total_seats': 150,
                'available_seats': 150,
            },
            {
                'title': 'Drama Play',
                'description': 'A captivating drama performance.',
                'date': date(2025, 5, 5),
                'time': time(18, 30),
                'total_seats': 80,
                'available_seats': 80,
            },
        ]

        for show_data in sample_shows:
            Show.objects.create(**show_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample shows.'))