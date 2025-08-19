from django.shortcuts import render
from .models import Schedule


def schedule_list(request):
    schedules = Schedule.objects.select_related("specialist")

    context = {
        "therapist_schedules": schedules.filter(location="therapists"),
        "pediatrician_schedules": schedules.filter(location="pediatricians"),
        "polyclinic_schedules": schedules.filter(location="polyclinic"),
        "ivenec_schedules": schedules.filter(location="ivenec"),
        "rakov_schedules": schedules.filter(location="rakov"),
    }

    return render(request, "schedule/schedule_list.html", context)
