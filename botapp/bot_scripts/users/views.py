from asgiref.sync import sync_to_async

from users.models import User


@sync_to_async
def get_user(telegram_id):
    return User.objects.get(telegram_id=telegram_id)


@sync_to_async
def get_user_by_telegram(telegram_username):
    return User.objects.get(telegram_username=telegram_username)


@sync_to_async
def edit_user_telegram_id(user, telegram_id):
    user.telegram_id = telegram_id
    return user.save()


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

# def get_user(tg_username):
#     @sync_to_async
#     def get():
#         return User.objects.get(telegram_username=tg_username)
#
#     async def get_loop():
#         return await get()
#
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_loop())
#     return loop.run_until_complete(get_loop())
#
#
# r = get_user('@OptikRUS')
# print(r.username, r.first_name, r.last_name)
