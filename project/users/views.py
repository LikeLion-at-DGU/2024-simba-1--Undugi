from django.shortcuts import render

# Create your views here.
def mypage(request):
    consumedCalorie = request.user.profile.consumedCalorie
    goal = request.user.profile.goal
    remainCalorie = goal  - consumedCalorie
    context = {
        'remainCalorie' : remainCalorie
    }
    return render(request, 'users/mypage.html', context)