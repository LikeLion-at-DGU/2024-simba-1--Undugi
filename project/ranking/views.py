from django.shortcuts import render
from .models import Ranking
from .utils import update_rankings

    
    ##rankings = Ranking.objects.order_by('-total_calories_burned')
    ##for index, ranking in enumerate(rankings, start=1):
    ##    ranking.rank = index
    ##    ranking.save()

def ranking_page(request):
    update_rankings()
    top_rankings = list(Ranking.objects.order_by('rank')[:6])
    user_ranking = None
    user_rank=None
    if request.user.is_authenticated:
        try:
           user_ranking = Ranking.objects.get(profile__user=request.user)
           user_rank = user_ranking.rank
           ##user_ranking = Ranking.objects.get(nickname=request.user.username)
        except Ranking.DoesNotExist:
            user_ranking = None

    context = {
        'top_rankings': top_rankings,
        'user_ranking': user_ranking,
        'user_rank' : user_rank,
    }
    return render(request, 'ranking/ranking.html', context)

def detailed_ranking_page(request):
    update_rankings()
    all_rankings = Ranking.objects.order_by('rank')
    context = {
        'all_rankings': all_rankings,
    }
    return render(request, 'ranking/detailed_ranking.html', context)
