from django.contrib import admin

from products.models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'description', ('category', 'price', 'quantity'), 'image',)
    search_fields = ('name', )
    ordering = ('price', )


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active')
