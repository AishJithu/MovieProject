from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from register.models import Users
from django.contrib.auth.hashers import check_password
from movie.models import Movies

#Signup
def signup(request):
    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password = request.POST['password']
        password = request.POST['password']
        user = Users.objects.filter(username=username).first()
        if user:
            return HttpResponse('username already exist')
        else:
            user = Users.objects.create(username=username, email=email, password=password, first_name=first_name, last_name=last_name,status=True,is_admin=False)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'signup.html')

#login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')      
        user = Users.objects.filter(username=username).first()
        if user:
            print(user.password)  
            print(password)
            if password == user.password:
                print(user.id)
                request.session['user_id'] = user.id
                return redirect('movie_list')
            else:
                return HttpResponse('Incorrect password')
        else:
            return HttpResponse('user not found')
    return render(request, 'login.html')

#View Profile
def view_profile(request):
    user_id = request.session.get('user_id')
    user = Users.objects.filter(id=user_id).first()
    movies = Movies.objects.filter(created_by=user_id)
    print("user",user_id)
    return render(request, 'profile.html', {'user': user, 'movies':movies})

def logout(request):
    try:
        del request.session["user_id"]
    except KeyError:
        pass
    return redirect('login')
    # return HttpResponse("You're logged out.")