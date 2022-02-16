from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField('аватар', upload_to='users_images', null=True, blank=True)
    telegram_id = models.PositiveIntegerField('телеграм ID', unique=True, null=True, blank=True)
    telegram_username = models.CharField('ник телеграм', max_length=64, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.telegram_username = f'@{self.telegram_username}'
    #     super(User, self).save(self, *args, **kwargs)
