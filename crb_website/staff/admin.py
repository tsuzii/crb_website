from django.contrib import admin
from .models import Specialist


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'category', 'is_active', 'order')
    list_editable = ('order',)
    list_filter = ('category', 'is_active')
    ordering = ('order',)
