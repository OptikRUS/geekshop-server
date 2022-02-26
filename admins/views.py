from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


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
            messages.success(request, 'Пользователь успешно создан!')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админка/Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Поздравляем! Профиль изменён успешно.')
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'Админка/Редактирование пользователя', 'form': form, 'selected_user': selected_user}
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
