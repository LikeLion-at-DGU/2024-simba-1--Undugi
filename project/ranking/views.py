from django.shortcuts import render
from .models import Ranking

def ranking_page(request):
    top_rankings = Ranking.objects.order_by('-total_calories_burned')[:3]
    user_ranking = Ranking.objects.get(nickname=request.user.username) if request.user.is_authenticated else None
    context = {
        'top_rankings': top_rankings,
        'user_ranking': user_ranking,
    }
    return render(request, 'ranking/ranking.html', context)

def detailed_ranking_page(request):
    all_rankings = Ranking.objects.order_by('-total_calories_burned')
    context = {
        'all_rankings': all_rankings,
    }
    return render(request, 'ranking/detailed_ranking.html', context)
