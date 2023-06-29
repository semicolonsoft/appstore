from django.urls import path
from accounts.views import *

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('user_profile', UserProfile.as_view()),
]
