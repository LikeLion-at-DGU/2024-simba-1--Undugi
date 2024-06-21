from django.shortcuts import render

# Create your views here.
def mypage(request):
    user = request.user
    profileImage = user.profile.profileImage if user.profile.profileImage else '/project/static/images/defaultProfile.jpg'
    consumedCalorie = request.user.profile.consumedCalorie
    goal = request.user.profile.goal
    remainCalorie = goal  - consumedCalorie
    context = {
        'profileImage': profileImage,
        'remainCalorie' : remainCalorie
    }
    return render(request, 'users/mypage.html', context)