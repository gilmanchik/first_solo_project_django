from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('здесь будет страница со всеми статьями')


def addpage(request):
    return HttpResponse('а здесь форма для добавления статей')
