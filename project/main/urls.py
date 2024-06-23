from django.urls import path, include
from .views import *
from main import views

app_name = "main"
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('map/', map_page, name='map_page'),
    path('arrive/', arrive, name='arrive'),
]