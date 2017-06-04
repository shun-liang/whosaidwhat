import pandas as pd

from django.core.management.base import BaseCommand
from django.db import transaction

from whosaidwhat.candidates.models import ElectionCandidate


class Command(BaseCommand):
    help = 'Upload candidates data from a CSV to the database'

    def add_arguments(self, parser):
        parser.add_argument('csv', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        data_frame = pd.read_csv(options['csv'])
        for _, row in data_frame.iterrows():
            ElectionCandidate.objects.update_or_create(
                name=row['name'],
                defaults={
                    'image_url': row['image_url'],
                    'facebook_page_url': row['facebook_personal_url'],
                    'twitter_username': row['twitter_username'],
                }
            )
