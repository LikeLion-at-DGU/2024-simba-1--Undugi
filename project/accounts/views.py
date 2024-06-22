from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(request, username=id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage') # alert(?)
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup1(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            request.session['id'] = request.POST['id']
            request.session['password'] = request.POST['password']
            return redirect('accounts:signup2')
    return render(request, 'accounts/signup.html')

def signup2(request):
    if request.method == 'POST':
        request.session['nickName'] = request.POST['nickName']
        request.session['major'] = request.POST['major']
        request.session['weight'] = request.POST['weight']
        request.session['gender'] = request.POST['gender']
        request.session['agegroup'] = request.POST['agegroup']
        return redirect('accounts:signup3')
    return render(request, 'accounts/signup2.html')

def signup3(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.session['id'],
            password=request.session['password']
        )
        user.profile.nickName = request.session['nickName']
        user.profile.major = request.session['major']
        user.profile.weight = request.session['weight']
        user.profile.gender = int(request.session['gender'])
        user.profile.agegroup = request.session['agegroup']

        user.profile.goal = request.POST['goal']

        user.profile.save()

        auth.login(request, user)
        return redirect('/')
    return render(request, 'accounts/signup3.html')

def idpasswordfind(request):
    return render(request, 'accounts/idpasswordfind.html')

def idfindv1(request):
    return render(request, 'accounts/idfindv1.html')

def idfindv2(request):
    return render(request, 'accounts/idfindv2.html')

def passwordfindv1(request):
    return render(request, 'accounts/passwordfindv1.html')

def passwordfindv2(request):
    return render(request, 'accounts/passwordfindv2.html')