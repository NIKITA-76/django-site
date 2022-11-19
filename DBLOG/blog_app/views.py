from django.shortcuts import render
from django.http import HttpResponseNotFound


def first_page(request):
    return render(request, 'first_page.html')


def mess_page(request):
    return render(request, 'messenger_page.html')


def tgBot_page(request):
    return render(request, 'tgBot_page.html')


def KivyApp_page(request):
    return render(request, 'KivyApp_page.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена брат")
