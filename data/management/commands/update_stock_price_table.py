import csv
from django.core.management.base import BaseCommand
from decimal import Decimal
from data.models import StockPrice

DATE = 0
OPEN = 1
CLOSE = 2
VOLUME = 3


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./TSLA.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # skip the headers
            for row in reader:
                sp = StockPrice.objects.get_or_create(date=row[DATE], defaults={
                    'open': Decimal(row[OPEN]),
                    'close': Decimal(row[CLOSE]),
                    'volume': int(row[VOLUME], 10),
                })
