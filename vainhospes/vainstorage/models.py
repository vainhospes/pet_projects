from django.db import models
from django.urls import reverse
import pytils


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=Product.Status.AVAILABLE)

class Product(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Отсутствует'
        AVAILABLE = 1, 'В наличий'

    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=False, db_index=True, verbose_name='Slug')
    season = models.ForeignKey('Season', on_delete=models.PROTECT, related_name='products', verbose_name='Сезон')
    description = models.TextField(blank=True, verbose_name='Описание')
    sell_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продажи')
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена покупки')
    is_available = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT , verbose_name='Наличие')
    tags = models.ManyToManyField('TagProduct', blank=True, related_name='tags', verbose_name='Тег')
    objects = models.Manager()
    available = AvailableManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежды"
        ordering = ['-sell_price']
        indexes = [
            models.Index(fields=['-sell_price']),
        ]

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.name)
        super().save(*args, **kwargs)

class Season(models.Model):
    name = models.CharField(max_length=100, verbose_name='Сезоны')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True)

    class Meta:
        verbose_name = 'Сезон'
        verbose_name_plural = 'Сезоны'

    def __str__(self):
        return self.name


class TagProduct(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})