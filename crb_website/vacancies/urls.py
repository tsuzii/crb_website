from django.urls import path
from .views import vacancies_list

urlpatterns = [
    path('', vacancies_list, name='vacancies'),
]
