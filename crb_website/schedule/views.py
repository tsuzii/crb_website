from django.shortcuts import render
from .models import Schedule


def schedule_list(request):
    specialists = Schedule.objects.all()
    return render(request, "schedule/schedule_list.html", {"specialists": specialists})
