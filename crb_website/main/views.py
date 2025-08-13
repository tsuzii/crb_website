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


def information(request):
    return render(request, 'main/information.html')


def information_section(request, section):
    templates = {
        'driving_comission': 'information/driving_comission.html',
        'palliative_care': 'information/palliative_care.html',
        'discounted_medicines': 'information/discounted_medicines.html',
        'unified_health_days': 'information/unified_health_days.html',
    }

    template = templates.get(section)
    if template:
        return render(request, template)
    else:
        raise Http404("Раздел не найден")


def services(request):
    return render(request, 'main/services.html')


def services_section(request, section):
    templates = {
        'kab_uzi': 'services/kab_uzi.html',
        'kab_func_diagnostic': 'services/kab_func_diagnostic.html',
        'kab_ endoscopy': 'services/kab_ endoscopy.html',
        'kab_diagnostic_lab': 'services/kab_diagnostic_lab.html',
        'kab_x_ray_diagnostic': 'services/kab_x_ray_diagnostic.html',
        'kab_kt': 'services/kab_kt.html',
    }

    template = templates.get(section)
    if template:
        return render(request, template)
    else:
        raise Http404("Раздел не найден")


def contacts(request):
    return render(request, 'main/contacts.html')
