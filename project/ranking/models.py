from django.db import models

class Ranking(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100, unique=True)
    total_calories_burned = models.FloatField()

    def __str__(self):
        return f"{self.nickname} - {self.total_calories_burned}"
