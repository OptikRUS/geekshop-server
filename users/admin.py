from django.contrib import admin

from users.models import User
from baskets.admin import BasketAdminInline


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
    list_display = ('username', 'first_name', 'last_name', 'telegram_username', 'is_superuser',
                    'is_staff', 'is_active', 'date_joined')
    fields = (
        'username', 'age',
        'email', ('first_name', 'last_name'),
        ('telegram_username', 'telegram_id'),
        ('is_superuser', 'is_staff', 'is_active'),
        'image',
        ('last_login', 'date_joined'),
        'groups', 'user_permissions',
        'password'
    )
    readonly_fields = ('password', 'telegram_id', 'last_login', 'date_joined')
    search_fields = ('username',)
