from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='main'),
    path('about/', about, name='about'),
    path('addpage', addpage, name='addpage')
]