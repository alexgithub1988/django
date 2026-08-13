from django.contrib import admin

from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']
    date_hierarchy = 'created_at'
    
    actions = ['make_free', 'increase_price_by_10_percent']
    
    def make_free(self, request, queryset):
        """Действие для установки цены 0 для выбранных товаров"""
        updated_count = queryset.update(price=0.00)
        self.message_user(
            request,
            f'{updated_count} товар(ов) теперь бесплатны.',
            level='SUCCESS'
        )
    make_free.short_description = "Сделать выбранные товары бесплатными"
    
    def increase_price_by_10_percent(self, request, queryset):
        """Действие для увеличения цены на 10% для выбранных товаров"""
        updated_count = 0
        for product in queryset:
            product.price = product.price * 1.10
            product.save()
            updated_count += 1
        self.message_user(
            request,
            f'Цена увеличена на 10% для {updated_count} товар(ов).',
            level='SUCCESS'
        )
    increase_price_by_10_percent.short_description = "Увеличить цену на 10%"

