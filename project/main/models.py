from django.db import models
from django.contrib.auth.models import User

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)  # 건물 이름
    
    def __str__(self):
        return self.name

class Visit(models.Model): 
    id = models.AutoField(primary_key=True)
    start_building = models.TextField()  # 시작 건물
    end_building = models.TextField()  # 도착 건물
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    # calorie = models.FloatField()  # 소모 칼로리 추가

    #def __str__(self):
    #    return f"Visit from {self.start_building} to {self.end_building} with {self.calorie} kcal"
