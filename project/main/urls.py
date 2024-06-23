from django.urls import path, include
from .views import *
from main import views

app_name = "main"
urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('map_select/', map_select, name='map_select'),
    path('map/<int:id>', map_page, name='map_page'),
    path('arrive/', arrive, name='arrive'),
]