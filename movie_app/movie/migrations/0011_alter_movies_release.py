# Generated by Django 4.2.11 on 2024-04-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_reviews_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='release',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]