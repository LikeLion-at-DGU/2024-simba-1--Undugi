from django.urls import path
from .views import ranking_page, detailed_ranking_page

app_name = "ranking"
urlpatterns = [
    path('ranking/', ranking_page, name='ranking_page'),
    path('ranking/detailed/', detailed_ranking_page, name='detailed_ranking_page'),
]