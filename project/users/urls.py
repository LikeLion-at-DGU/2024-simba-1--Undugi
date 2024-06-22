from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "users"
urlpatterns = [
    path('mypage', mypage, name="mypage"),
    path('modify', modify, name="modify"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)