from django.db import models

# Create your models here.

class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)  # 건물 이름

    def __str__(self):
        return self.name

class Visit(models.Model): 
    id = models.AutoField(primary_key=True)
    start_building = models.ForeignKey(Building, related_name='start_visits', on_delete=models.CASCADE)  # 시작 건물
    end_building = models.ForeignKey(Building, related_name='end_visits', on_delete=models.CASCADE)  # 도착 건물

    def __str__(self):
        return f"Visit from {self.start_building} to {self.end_building}"

class Path(models.Model): 
    id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=30)  # 길
    calorie = models.FloatField()  # 소모 칼로리
    degree = models.FloatField()  # 각도
    speed = models.FloatField()  # 속도

    def __str__(self):
        return self.path

class Route(models.Model):
    id = models.AutoField(primary_key=True)
    start_building = models.ForeignKey(Building, related_name='start_routes', on_delete=models.CASCADE)  # 시작 건물
    end_building = models.ForeignKey(Building, related_name='end_routes', on_delete=models.CASCADE)  # 도착 건물
    path = models.ForeignKey(Path, on_delete=models.CASCADE)  # 경로
    calorie = models.FloatField()  # 소모 칼로리

    def __str__(self):
        return f"Route from {self.start_building} to {self.end_building} via {self.path}"
