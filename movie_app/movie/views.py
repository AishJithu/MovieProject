from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from movie.models import Movies, Reviews
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Q  # Import the Q object

from register.models import Users

def movie(request):
    movies = Movies.objects.filter()
    return render(request, 'movie_list.html', {'movies': movies})

def create_movie(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
           
        title = request.POST['title']
        poster = request.POST['poster']
        description = request.POST['description']
        release = request.POST['release']
        actors = request.POST['actors']
        category = request.POST['category']
        genre = request.POST['genre']
        status = True
        created_by =user_id
        created_at = datetime.now()
        updated_at = datetime.now()
        user = Movies.objects.create(title=title, poster=poster,description=description,release=release,actors=actors,category=category,genre=genre,status=status,created_at=created_at,updated_at=updated_at)
        user.save()
        messages.success(request, 'Movie created successfully')
        return redirect('movie_list')
    return render(request, 'create_movie.html')


def movie_list(request):
    movies = Movies.objects.filter()
    user_id = request.session.get('user_id')
    user = Users.objects.filter(id=user_id).first()
    return render(request, 'movie_list.html', {'movies': movies, 'user':user})


def movie_details(request, movie_id):
    user_id = request.session.get('user_id')
    user = Users.objects.filter(id=user_id).first()
    reviews = Reviews.objects.filter(movie=movie_id)
    print("user",user_id)
    data = Movies.objects.filter(id=movie_id)
    return render(request, 'movie_details.html', {'movie': data, 'user':user, 'reviews':reviews})


def search_movies(request, query):
    print(query)
    movies = Movies.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    return render(request, 'movie_list.html', {'movies': movies})



def edit_movie(request, movie_id):
    user_id = request.session.get('user_id')
    user = Users.objects.filter(id=user_id).first()
    print("user",user_id)
    data = Movies.objects.filter(id=movie_id)
    return render(request, 'edit_movie.html', {'movie': data, 'user':user})

def create_review(request, movie_id):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        # movie = movie_id
        user = Users.objects.filter(id=user_id).first()
        user_name = user.first_name
        description = request.POST['description']
        created_at = datetime.now()
        updated_at = datetime.now()
        _movie = Reviews.objects.create(movie=movie_id, user_id=user_id, user_name=user_name, description=description, created_at=created_at, updated_at=updated_at)
        _movie.save()
        messages.success(request, 'Review created successfully')
        
        print(movie_id, user_id, description)
        return redirect('movie_list')
    return render(request, 'movie_list.html')

 
# def update(request,id):
#     movie = Movies.objects.get(id=id)
#     form = MovieForm(request.POST or None, request.FILES, instance=movie)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'update.html',{'form':form,'movie':movie})

def delete_movies(request,movie_id):
    if request.method=='POST':
        movie=Movies.objects.get(id=movie_id)
        print(movie)
        if movie:
            movie.delete()
            return HttpResponse('Movie Deleted')
        else:
            return HttpResponse('Movie not Deleted')
    # return render(request,'delete.html')
    return HttpResponse('Movie Deleted res')
   


