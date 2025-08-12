from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('about/<str:section>/', views.about_section, name='about_section'),

    path('services/', views.services, name='services'),
    path('services/<str:section>/',
         views.services_section, name='services_section'),

    path('contacts/', views.contacts, name='contacts'),

    path('information/', views.information, name='information'),
    path('information/<str:section>/',
         views.information_section, name='information_section'),
]
