from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная',
        'values': ["some", 'hi', '1234']
    }
    return render(request, 'main_page.html', data)


def about(request):
    return render(request, 'about.html', {'title': 'Про нас'})
