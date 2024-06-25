from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #id, password, name 전송
    nickName = models.TextField(max_length=30,unique=True)  # 닉네임
    profileImage = models.ImageField(upload_to='profileImages/', null=True)  # 프로필사진
    goal = models.FloatField(null=True)         # 목표소모칼로리
    consumedCalorie = models.FloatField(null=True, default=0)  # 총 소모한칼로리
    daily_consumedCalorie = models.FloatField(null=True, default=0) # 오늘 소모한 칼로리
    weight = models.FloatField(null=True, default=50)       # null False면 왜 오류?
    major = models.TextField(max_length=40)     # 소속 학과
    gender = models.BooleanField(null=True)               # 성별
    agegroup = models.IntegerField(null=True)            # 연령대
    # rank =  models.ForeignKey(Rank, null=True, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

