from django.db import models


class StockPrice(models.Model):
    class Meta:
        db_table = "stock_price"

    date = models.DateField(primary_key=True)
    open = models.DecimalField(max_digits=8, decimal_places=2)
    close = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.IntegerField()
