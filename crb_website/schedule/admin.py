from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "get_name",
        "get_speciality",
        "location",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
    )
    # фильтр по месту и должности
    list_filter = ("location", "specialist__position")
    # поиск по ФИО и должности
    search_fields = ("specialist__name", "specialist__position")

    def get_name(self, obj):
        return obj.specialist.name
    get_name.short_description = "Ф.И.О."

    def get_speciality(self, obj):
        return obj.specialist.position
    get_speciality.short_description = "Специальность"
