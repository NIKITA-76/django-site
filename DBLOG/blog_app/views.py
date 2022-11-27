from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *


def first_page(request):
    posts = ModelPost.objects.all()
    return render(request, 'main.html', {'posts': posts}, )


def contact(request):
    posts = ModelPost.objects.all()
    return render(request, 'contact_mail.html', {'posts': posts}, )


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена брат")
