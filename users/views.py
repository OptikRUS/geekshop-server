from django.shortcuts import render


def login(request):
    context = {
        'title': 'авторизация',
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'регистрация',
    }
    return render(request, 'users/register.html', context)
