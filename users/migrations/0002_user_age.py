# Generated by Django 3.2.12 on 2022-02-17 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True, verbose_name='возраст'),
        ),
    ]
