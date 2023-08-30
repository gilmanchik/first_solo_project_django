from django.shortcuts import render
from .models import *


def index(request):
    data = Information.objects.order_by('title')
    return render(request, 'main_page.html', {'data': data})


def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})
