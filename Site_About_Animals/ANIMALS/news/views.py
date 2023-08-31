from django.shortcuts import render, redirect
from .forms import *


def news_home(request):
    context = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'context': context})


def create_news(request):
    error = ''
    if request.method == 'POST':
        forms = ArticlesForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('news_home')
        else:
            error = 'Неправильные данные'

    form = ArticlesForm()
    date = {
        'form': form,
        'error': error
    }

    return render(request, 'create_news.html', date)