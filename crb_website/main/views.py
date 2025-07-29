from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def information(request):
    return render(request, 'main/information.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def history(request):
    return render(request, 'main/history.html')
