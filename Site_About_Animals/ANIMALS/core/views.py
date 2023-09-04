from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    data = Information.objects.order_by('title')
    return render(request, 'main_page.html', {'data': data})


def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})


class InfoDetail(DetailView):
    model = Information
    template_name = 'info_detail.html'
    context_object_name = 'info_post'


class InfoUpdate(UpdateView):
    model = Information
    template_name = 'create_info.html'
    form_class = InformationForm


class InfoDelete(DeleteView):
    model = Information
    template_name = 'delete_info.html'
    success_url = '/'


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
