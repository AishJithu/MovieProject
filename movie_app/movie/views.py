from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import HttpResponseRedirect



from movie.models import Movies, Reviews
from django.contrib import messages
from django.db.models import Q  # Import the Q object

from register.models import Users
from django.shortcuts import render, get_object_or_404, redirect

# from .models import Movies, Users, Reviews
from .forms import MovieForm
from .forms import UploadFileForm


def movie(request):
    movies = Movies.objects.filter()
    return render(request, 'movie_list.html', {'movies': movies})

# def create_movie(request):
#     if request.method == 'POST':
#         _user_id = request.session.get('user_id')

#         release_date_str = request.POST['release']
#         release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()

#         title = request.POST['title']
#         # poster = request.POST['poster']
#         description = request.POST['description']
#         release = datetime.combine(release_date, datetime.min.time())
#         actors = request.POST['actors']
#         category = request.POST['category']
#         genre = "null"
#         status = True
#         created_by = _user_id
#         created_at = datetime.now()
#         updated_at = datetime.now()

#         print("poster--> ",poster)
        
#         if 'poster' in request.FILES:
#             poster = request.FILES['poster']
#         else:
#             poster = None

#         user = Movies.objects.create(title=title, poster=poster,description=description,release=release,actors=actors,category=category,genre=genre,status=status,created_by=created_by,created_at=created_at,updated_at=updated_at)
#         user.save()
#         messages.success(request, 'Movie created successfully')
#         return redirect('movie_list')
#     return render(request, 'create_movie.html')

def create_movie(request):
    if request.method == 'POST':
        _user_id = request.session.get('user_id')

        release_date_str = request.POST['release']
        release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()

        title = request.POST['title']
        description = request.POST['description']
        release = datetime.combine(release_date, datetime.min.time())
        actors = request.POST['actors']
        category = request.POST['category']
        trailer = request.POST['trailer']
        genre = "null"
        status = True
        created_by = _user_id
        created_at = datetime.now()
        updated_at = datetime.now()

        # Initialize poster with None
        poster = None

        # Check if a file is uploaded
        if 'poster' in request.FILES:
            poster = request.FILES['poster']

        movie = Movies.objects.create(
            title=title, 
            poster=poster, 
            description=description, 
            release=release, 
            actors=actors, 
            category=category, 
            genre=genre, 
            status=status, 
            trailer=trailer, 
            created_by=created_by, 
            created_at=created_at, 
            updated_at=updated_at
        )
        movie.save()
        messages.success(request, 'Movie created successfully')
        return redirect('movie_list')
    return render(request, 'create_movie.html')

# def create_movie(request):
#     _user_id = request.session.get('user_id')
#     print("user",_user_id)
#     if request.method == 'POST':
#         form = MovieForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('movie_list', {'user':_user_id})  # Redirect to a URL name of your choice
#     else:
#         form = MovieForm()
#     return render(request, 'create_movie.html', {'form': form})

def upload_file(request):
    print('upload')
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def handle_uploaded_file(f):
    with open("movie_.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
            

def movie_list(request):
    movies = Movies.objects.filter()
    user_id = request.session.get('user_id')
    user = Users.objects.filter(id=user_id).first()
    return render(request, 'movie_list.html', {'movies': movies, 'user':user})

def movie_details(request, movie_id):
    user_id = request.session.get('user_id')
    user = Users.objects.filter(id=user_id).first()
    reviews = Reviews.objects.filter(movie=movie_id)
    data = Movies.objects.filter(id=movie_id)
    return render(request, 'movie_details.html', {'movie': data, 'user':user, 'reviews':reviews})

def search_movies(request, query):
    print(query)
    movies = Movies.objects.filter(Q(title__icontains=query) | Q(category__icontains=query))
    return render(request, 'movie_list.html', {'movies': movies})

def edit_movie(request, movie_id):
    movie = get_object_or_404(Movies, pk=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        print("form 1-->",form)
        print("form.errors -->",form.errors)
        if form.is_valid():
            
            print("form 2 -->",form)
            form.save()
            return redirect('movie_details', movie_id=movie_id)
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

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

def update_movie(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    print("_movie",movie)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'edit_movie.html', {'form': form})

def delete_movies(request, movie_id):
    print(movie_id)
    user = Movies.objects.filter(id=movie_id).first()
    user.delete()
    return redirect('movie_list')


