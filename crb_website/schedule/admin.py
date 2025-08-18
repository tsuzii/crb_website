from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "speciality",
        "location",   # добавил поле место приёма
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
    )
    # фильтрация по специальности и месту приёма
    list_filter = ("speciality", "location")
    search_fields = ("name", "speciality")  # поиск по ФИО и специальности
