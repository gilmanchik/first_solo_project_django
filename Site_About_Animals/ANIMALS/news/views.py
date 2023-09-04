from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    context = Articles.objects.order_by('-date')
    return render(request, 'news_home.html', {'context': context})


class NewsDetail(DetailView):
    model = Articles
    template_name = 'news_detail.html'
    context_object_name = 'news_post'


class NewsUpdate(UpdateView):
    model = Articles
    template_name = 'create_news.html'
    form_class = ArticlesForm


class NewsDelete(DeleteView):
    model = Articles
    template_name = 'delete_news.html'
    success_url = '/'


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
