from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *


def first_page(request):
    posts = ModelPost.objects.all()
    return render(request, 'main.html', {'posts': posts})


def mess_page(request):
    return render(request, 'messenger_page.html')


def tgBot_page(request):
    return render(request, 'tgBot_page.html')


def KivyApp_page(request):
    return render(request, 'KivyApp_page.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена брат")
