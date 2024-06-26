# ranking/utils.py
from accounts.models import Profile
from .models import Ranking


def update_rankings():
    # 프로필 데이터를 소모한 칼로리 내림차순으로 정렬하여 가져옴
    profiles = Profile.objects.all().order_by('-consumedCalorie')
     # 각 프로필에 대해 랭킹을 업데이트
    for index, profile in enumerate(profiles, start=1):
        # 프로필에 해당하는 랭킹 객체를 가져오거나 생성
        ranking, created = Ranking.objects.get_or_create(profile=profile)
         # 총 소모한 칼로리와 랭킹을 업데이트
        ranking.total_calories_burned = profile.consumedCalorie
        ranking.rank = index
        ranking.save()