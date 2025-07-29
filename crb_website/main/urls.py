from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('about/history', views.history, name='history'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('information', views.information, name='information'),
]
