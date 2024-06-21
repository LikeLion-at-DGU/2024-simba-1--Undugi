from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup1, name="signup1"),
    path('signup2/', signup2, name="signup2"),
    path('idpasswordfind/', idpasswordfind, name="idpasswordfind"),
    path('idfindv1/', idfindv1, name="idfindv1"),
    path('idfindv2/', idfindv2, name="idfindv2"),
    path('passwordfindv1/', passwordfindv1, name="passwordfindv1"),
    path('passwordfindv2/', passwordfindv2, name="passwordfindv2"),
]