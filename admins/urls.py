from django.urls import path

from admins.views import index, AdminUserListView, AdminUserCreateView, AdminUserUpdateView, AdminUserDeleteView, \
    AdminCategoryListView, AdminCategoryCreateView, AdminCategoryUpdateView, AdminCategoryDeleteView, \
    AdminProductListView, AdminProductCreateView, AdminProductUpdateView, AdminProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', AdminUserListView.as_view(), name='admin_users'),
    path('users-create/', AdminUserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', AdminUserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', AdminUserDeleteView.as_view(), name='admin_users_delete'),
    path('categories/', AdminCategoryListView.as_view(), name='admin_categories'),
    path('category-create/', AdminCategoryCreateView.as_view(), name='admin_category_create'),
    path('category-update/<int:pk>/', AdminCategoryUpdateView.as_view(), name='admin_category_update'),
    path('category-delete/<int:pk>/', AdminCategoryDeleteView.as_view(), name='admin_category_delete'),
    path('products/', AdminProductListView.as_view(), name='admin_products'),
    path('product-create/', AdminProductCreateView.as_view(), name='admin_product_create'),
    path('product-update/<int:pk>/', AdminProductUpdateView.as_view(), name='admin_product_update'),
    path('product-delete/<int:pk>/', AdminProductDeleteView.as_view(), name='admin_product_delete'),
]
