from django.contrib import admin

from baskets.models import Basket


@admin.register(Basket)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
    fields = ('user', ('product', 'quantity'), 'created_timestamp', )
    readonly_fields = ('created_timestamp',)
    search_fields = ('user', )
    ordering = ('user', )


class BasketAdminInline(admin.TabularInline):
    model = Basket
    readonly_fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
