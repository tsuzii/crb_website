from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "speciality",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
    )
    list_filter = ("speciality",)  # фильтрация по специальности
    search_fields = ("name", "speciality")  # поиск по ФИО и специальности
