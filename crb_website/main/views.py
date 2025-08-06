from django.shortcuts import render
from django.http import Http404
# Create your views here.


def index(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def about_section(request, section):
    templates = {
        'departments': 'about/departments.html',
        'history': 'about/history.html',
        'trade_union': 'about/trade_union.html',
        'procedures': 'about/procedures.html',
        'media': 'about/media.html',
        'rating_score': 'about/rating_score.html',
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
