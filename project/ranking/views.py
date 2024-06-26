from django.shortcuts import render
from .models import Ranking
from .utils import update_rankings

# 랭킹 페이지를 렌더링하는 뷰 함수
def ranking_page(request):
    # 랭킹 업데이트 함수 호출
    update_rankings()
    top_rankings = list(Ranking.objects.order_by('rank')[:5])
    user_ranking = None
    user_rank=None
    # 사용자가 인증된 상태인지 확인
    if request.user.is_authenticated:
        try:
           # 현재 로그인된 사용자의 랭킹 정보를 가져옴
           user_ranking = Ranking.objects.get(profile__user=request.user)
           user_rank = user_ranking.rank
        except Ranking.DoesNotExist:
            # 사용자의 랭킹 정보가 없을 경우 None으로 설정
            user_ranking = None
# 템플릿에 전달할 컨텍스트 데이터 설정
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
