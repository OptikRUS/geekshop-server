from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField('аватар', upload_to='users_images', null=True, blank=True)
    telegram_id = models.PositiveIntegerField('телеграм ID', unique=True, null=True, blank=True)
    telegram_username = models.CharField('ник телеграм', max_length=64, null=True, blank=True)
    age = models.PositiveIntegerField('возраст', null=True)

    def __str__(self):
        return self.username

    def safe_delete(self):
        self.is_active = False
        self.save()
