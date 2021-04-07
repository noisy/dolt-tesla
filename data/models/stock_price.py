from django.db import models


class StockPrice(models.Model):
    class Meta:
        db_table = "stock_price"

    date = models.TextField(primary_key=True)
    open = models.DecimalField(max_digits=8, decimal_places=2)
    high = models.DecimalField(max_digits=8, decimal_places=2)
    low = models.DecimalField(max_digits=8, decimal_places=2)
    close = models.DecimalField(max_digits=8, decimal_places=2)
    adj_close = models.DecimalField(max_digits=8, decimal_places=2)
    volume = models.IntegerField()
