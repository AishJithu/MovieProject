# Generated by Django 4.2.11 on 2024-04-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_alter_movies_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
