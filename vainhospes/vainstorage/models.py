from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField (max_length=100)
    description = models.TextField(blank=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)