# ranking/utils.py
from accounts.models import Profile
from .models import Ranking

def update_rankings():
    profiles = Profile.objects.all().order_by('-consumedCalorie')
    for index, profile in enumerate(profiles, start=1):
        ranking, created = Ranking.objects.get_or_create(profile=profile)
        ranking.total_calories_burned = profile.consumedCalorie
        ranking.rank = index
        ranking.save()