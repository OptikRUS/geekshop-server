from django.urls import path

from admins.views import index, AdminUserListView, AdminUserCreateView, AdminUserUpdateView, AdminUserDeleteView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', AdminUserListView.as_view(), name='admin_users'),
    path('users-create/', AdminUserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<int:pk>/', AdminUserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<int:pk>/', AdminUserDeleteView.as_view(), name='admin_users_delete'),
]


