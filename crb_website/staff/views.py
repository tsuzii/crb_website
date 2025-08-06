from django.shortcuts import render
from .models import Specialist


def specialists_list(request):
    specialists = Specialist.objects.filter(category='general', is_active=True)
    return render(request, 'staff/specialists_list.html', {'specialists': specialists})


def administration_view(request):
    admins = Specialist.objects.filter(
        category='admin', is_active=True).order_by('order')
    return render(request, 'staff/administration.html', {'specialists': admins})
