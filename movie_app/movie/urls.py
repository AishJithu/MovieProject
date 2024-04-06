from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie, name='movie'),
    path('create/', views.create_movie, name='create_movie'),
    path('create_review/<int:movie_id>', views.create_review, name='create_review'),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_details/<int:movie_id>/', views.movie_details, name='movie_details'),
    path('search_movies/<str:query>/', views.search_movies, name='search_movies'),
    path('delete_movies/<int:movie_id>/', views.delete_movies, name='delete_movies'),
]
