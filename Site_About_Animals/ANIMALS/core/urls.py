from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='main_page'),
    path('about/', about, name='about'),
    path('create_info/', create_info, name='create_info')
]