from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm


def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


def admin_users(request):
    users = User.objects.all()
    context = {
        'title': 'Админка/Пользователи',
        'users': users,
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админка/Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)
