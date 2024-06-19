from django.urls import path
from .views import *

app_name = "accounts"
urlpatterns = [
    path('login/', login, name="login"),
    path('signup/', signup1, name="signup1"),
    path('signup2/', signup2, name="signup2"),
]