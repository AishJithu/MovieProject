from django.db import models
from django.contrib.auth.models import User as DjangoUser


class Movies(models.Model):
    title = models.CharField(max_length=255)
    poster = models.CharField(max_length=255)
    description = models.TextField()  # Changed to TextField for long text
    release = models.DateField()  # Removed max_length, DateField does not need it
    actors = models.CharField(max_length=255)  # This could be a ManyToManyField if actors are related to multiple movies
    category = models.CharField(max_length=255)  # Changed to CharField assuming it's a category name
    genre = models.CharField(max_length=255)  # Changed 'gener' to 'genre', assuming it's the movie genre
    status = models.BooleanField(default=True)  # Changed default to True assuming it's active by default
    created_by = models.IntegerField()  # Changed to DateTimeField with auto_now_add for creation timestamp
    created_at = models.DateTimeField(auto_now_add=True)  # Changed to DateTimeField with auto_now_add for creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Changed to DateTimeField with auto_now for update timestamp


class Reviews(models.Model):
    movie= models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=225, default=True)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)