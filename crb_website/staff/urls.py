from django.urls import path
from .views import specialists_list

urlpatterns = [
    path('', specialists_list, name='specialists_list'),
]
