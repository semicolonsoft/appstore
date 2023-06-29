from django.urls import path
from store.views import *

urlpatterns = [
    path('application', ApplicationView.as_view()),
    path('application/<int:application_id>', ApplicationView.as_view()),
]
