from apscheduler.schedulers.background import BackgroundScheduler
from django.contrib.auth.models import User
from accounts.models import Profile
from datetime import datetime

# 자정마다 daily_consumedCalorie 초기화
def reset_daily_consumed_calorie():
    users = User.objects.all()
    for user in users:
        try:
            profile = Profile.objects.get(user=user)
            profile.reset_daily_consumedCalorie()
        except Profile.DoesNotExist:
            pass

# APScheduler 설정
scheduler = BackgroundScheduler()
scheduler.add_job(reset_daily_consumed_calorie, 'cron', hour=0, minute=0)
scheduler.start()