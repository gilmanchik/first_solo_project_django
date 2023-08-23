from django.shortcuts import render


def index(request):
    return render(request, 'main_page.html')


def addpage(request):
    return render(request, 'addpage.html')


def about(request):
    return render(request, 'about.html')
