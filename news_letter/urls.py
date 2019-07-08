from django.urls import path, re_path
from .views import *

app_name= 'news_letter'

urlpatterns = [
    path('', news_letter, name = 'news_letter'),
]