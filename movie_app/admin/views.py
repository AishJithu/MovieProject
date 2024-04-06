from django.shortcuts import render
from django.http import HttpResponse
from movie.models import Movies, Reviews
from register.models import Users


# Create your views here.
def admin_users(request):
    users = Users.objects.filter()
    return render(request, 'admin_users.html', {'users': users})

def admin_movies(request):
    movies = Movies.objects.filter()
    return render(request, 'admin_movies.html', {'movies': movies})


def admin_panel(request):
    movies = Movies.objects.filter()
    return render(request, 'admin_panel.html', {'movies': movies})