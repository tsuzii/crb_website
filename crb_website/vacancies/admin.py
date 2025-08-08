from django.contrib import admin
from .models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'category', 'is_active')
    list_filter = ('category', 'is_active')
