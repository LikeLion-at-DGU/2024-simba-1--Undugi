from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserProfileForm
from django.contrib.auth.hashers import make_password
# Create your views here.
def mypage(request):
    user = request.user
    profileImage = user.profile.profileImage if user.profile.profileImage else '/project/static/images/defaultProfile.jpg'
    consumedCalorie = request.user.profile.consumedCalorie
    goal = request.user.profile.goal
    
    if goal is None:
        goal=0.0
    if consumedCalorie is None:
        consumedCalorie=0.0    
    
    remainCalorie = goal  - consumedCalorie
    context = {
        'profileImage': profileImage,
        'remainCalorie' : remainCalorie
    }
    return render(request, 'users/mypage.html', context)


def modify(request):
    return render(request, 'users/modify.html')

def pw_checking(request):
    return render(request, 'users/pw_checking.html')

def modifyv2(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if profile_form.is_valid():
            profile_form.save()
            update_session_auth_hash(request, request.user)  # Important, to update the session with the new user info
            return redirect('users:mypage')
        else:
            # Handle errors if form is invalid
            print(profile_form.errors)
    else:
        profile_form = UserProfileForm(instance=request.user.profile)
    
    context = {
        'profile_form': profile_form,
    }
    return render(request, 'users/modifyv2.html', context)