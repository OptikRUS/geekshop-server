from django.shortcuts import render

from users.models import User


def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


def admin_users(request):
    users = User.objects.all()
    context = {
        'title': 'Админ-панель/Пользователи',
        'users': users,
    }
    return render(request, 'admins/admin-users-read.html', context)
