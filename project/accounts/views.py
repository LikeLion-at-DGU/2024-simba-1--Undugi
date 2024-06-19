from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(request, id=id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage') # alert(?)
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def login_view(request):
    return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                id=request.POST['id'],
                password=request.POST['password']
            )
            user.profile.nickname=request.POST['nickname']
            user.profile.weight=request.POST['weight']
            user.profile.goal=request.POST['goal']
            user.profile.place=request.POST['place']

            user.profile.save()

            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')