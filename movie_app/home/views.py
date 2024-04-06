from django.shortcuts import render
from django.http import HttpResponse
from register.models import Users
from movie.models import Movies


# Create your views here.
def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Users.objects.filter(id=user_id).first()
        
        movies = Movies.objects.filter()
        return render(request, 'movie_list.html', {'movies': movies,'user':user})
    else:
        return render(request, 'home.html')
        
