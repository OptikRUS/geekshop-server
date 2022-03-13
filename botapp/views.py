from asgiref.sync import sync_to_async

from users.models import User


@sync_to_async
def get_user(telegram_id):
    return User.objects.get(telegram_id=telegram_id)


@sync_to_async
def edit_profile(user, first_name, last_name, age, telegram_username):
    user.first_name = first_name
    user.last_name = last_name
    user.age = age
    user.telegram_username = telegram_username
    return user.save()


@sync_to_async
def exist_user(username):
    return User.objects.filter(username=username).exists()


@sync_to_async
def register_user(username, first_name, last_name, email, password, age, telegram_username, telegram_id):
    return User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        age=age,
        telegram_username=telegram_username,
        telegram_id=telegram_id
    )