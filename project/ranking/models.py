from django.db import models
from accounts.models import Profile


class Ranking(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='ranking', null=True)
    total_calories_burned = models.FloatField(default=0)
    rank = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nickname} - {self.total_calories_burned}"
