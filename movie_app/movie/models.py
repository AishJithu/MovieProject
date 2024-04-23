from django.db import models
from django.contrib.auth.models import User as DjangoUser


class Movies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    actors = models.CharField(max_length=255)  
    category = models.CharField(max_length=255)  
    genre = models.CharField(max_length=255)  
    status = models.BooleanField(default=True)  
    release = models.DateField(auto_now_add=True)
    created_by = models.IntegerField()  
    created_at = models.DateField(auto_now_add=True)  
    updated_at = models.DateField(auto_now=True)  
    poster = models.ImageField(null=True, blank=True, upload_to="images/")
    trailer = models.CharField(null=True, blank=True, max_length=255)  
    

class Reviews(models.Model):
    movie= models.IntegerField()
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=225, default=True)
    description = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)