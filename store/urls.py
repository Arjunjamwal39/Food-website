from .views import index, about, practice, register
from django.urls import path

urlpatterns = [
    path('', index),
    path('about/', about),
    path('index/', index),
    path('practice/', practice),
    path('register/', register),
]
