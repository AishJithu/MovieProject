# Generated by Django 4.2.11 on 2024-04-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_alter_movies_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='release',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
