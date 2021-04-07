import csv
from django.core.management.base import BaseCommand
from decimal import Decimal
from data.models import StockPrice

DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
ADJ_CLOSE = 5
VOLUME = 6


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./TSLA.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader, None)  # skip the headers
            for row in reader:
                if not StockPrice.objects.filter(date=row[DATE]).exists():
                    stock_price = StockPrice.objects.create(
                        date=row[DATE],
                        open=Decimal(row[OPEN]),
                        high=Decimal(row[HIGH]),
                        low=Decimal(row[LOW]),
                        close=Decimal(row[CLOSE]),
                        adj_close=Decimal(row[ADJ_CLOSE]),
                        volume=int(row[VOLUME], 10)
                    )
                    print(stock_price)
