from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('services', views.services),
    path('contacts', views.contacts),
    path('information', views.information),
]
