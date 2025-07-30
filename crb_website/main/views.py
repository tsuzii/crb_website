from django.shortcuts import render
from django.http import Http404
# Create your views here.


def index(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def about_section(request, section):
    templates = {
        'administration': 'about/administration.html',
        'departments': 'about/departments.html',
        'history': 'about/history.html',
        'specialists': 'about/specialists.html',
        'trade_union': 'about/trade_union.html',
        'procedures': 'about/procedures.html',
        'media': 'about/media.html',
    }

    template = templates.get(section)
    if template:
        return render(request, template)
    else:
        raise Http404("Раздел не найден")


def services(request):
    return render(request, 'main/services.html')


def information(request):
    return render(request, 'main/information.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def history(request):
    return render(request, 'main/history.html')
