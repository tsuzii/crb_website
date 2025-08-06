from django.urls import path
from .views import specialists_list, administration_view

urlpatterns = [
    path('', specialists_list, name='specialists_list'),
    path('administration/', administration_view, name='administration_list'),
]
