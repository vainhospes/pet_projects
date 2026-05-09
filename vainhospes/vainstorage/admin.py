from django.contrib import admin, messages
from .models import Product, Season


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'slug','season', 'description', 'sell_price', 'buy_price', 'tags']
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'season','sell_price', 'buy_price', 'is_available','brief_info')
    list_display_links = ('name',)
    # readonly_fields = ('slug',)
    filter_horizontal = ('tags',)

    ordering = ('name', 'id')
    list_editable = ('is_available',)
    list_per_page = 5
    actions = ['set_available', 'unset_available']
    search_fields = ('name__startswith','season__name')
    list_filter = ('season__name','is_available',)

    @admin.display(description='Содержание', ordering='description')
    def brief_info(self, product: Product):
        return f"Описание {len(product.description)} символов"

    @admin.action(description='Установать наличие продукта')
    def set_available(self, request, queryset):
        count = queryset.update(is_available=True)
        self.message_user(request, f"Теперь в наличий {count} товаров")

    @admin.action(description='Снять наличие продукта')
    def unset_available(self, request, queryset):
        count = queryset.update(is_available=True)
        self.message_user(request, f"Теперь в нету в наличий {count} товаров", messages.WARNING)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
