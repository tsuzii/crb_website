from django.shortcuts import render
from .models import Schedule


def schedule_list(request):
    schedules = Schedule.objects.select_related("specialist").all()
    return render(request, "schedule/schedule_list.html", {"schedules": schedules})
