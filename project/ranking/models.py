from django.db import models

# Create your models here.

class Ranking(models.Model):
    ranking_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100)
    total_calories_burned = models.FloatField()
    rank = models.IntegerField()

    def __str__(self):
        return f"{self.nickname} - {self.rank}"
