from django.shortcuts import render, redirect
from .forms import *


def index(request):
    data = Information.objects.order_by('title')
    return render(request, 'main_page.html', {'data': data})


def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})


def create_info(request):
    error = ''
    if request.method == "POST":
        forms = InformationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('main_page')
        else:
            error = 'Неверные данные'

    form = InformationForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create_info.html', data)
