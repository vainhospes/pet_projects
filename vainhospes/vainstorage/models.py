from django.db import models
from django.urls import reverse


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=Product.Status.AVAILABLE)

class Product(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Отсутствует'
        AVAILABLE = 1, 'В наличий'

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=False, db_index=True)
    season = models.ForeignKey('Season', on_delete=models.PROTECT, related_name='products')
    description = models.TextField(blank=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(choices=Status.choices, default=Status.AVAILABLE)
    tags = models.ManyToManyField('TagProduct', blank=True, related_name='tags')
    objects = models.Manager()
    available = AvailableManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-sell_price']
        indexes = [
            models.Index(fields=['-sell_price']),
        ]

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Season(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.name


class TagProduct(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})