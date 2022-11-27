from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import *

from blog_app import forms


def first_page(request):
    posts = ModelPost.objects.all()
    return render(request, 'main.html', {'posts': posts}, )


def contact(request):
    if request.method == 'POST':
        form = forms.SendToMail(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = forms.SendToMail()
    return render(request, 'contact_mail.html', {'form': form}, )


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена брат")
