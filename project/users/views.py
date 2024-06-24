from django.shortcuts import render

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
    return render(request, 'users/modifyv2.html')