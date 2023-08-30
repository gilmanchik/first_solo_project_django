from django.shortcuts import render
from .models import *


def news_home(request):
    context = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'context': context})
