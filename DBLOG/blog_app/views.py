from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

import requests
from bs4 import BeautifulSoup
import json
from blog_app import models
from blog_app import forms

import blog_app


def first_page(request):
    print(request)
    posts = models.ModelPost.objects.all()
    dict_r = {}
    if request.user.is_authenticated:
        query = """
        query ($login: String!) {
          viewer {
            login
            name
          }
          repositoryOwner(login: $login) {
            id
            repositories(
              isFork: false
              orderBy: {direction: DESC, field: PUSHED_AT}
              ownerAffiliations: OWNER
              last: 100
            ) {
              edges {
                node {
                  name
                  description
                  url
                  openGraphImageUrl
                  isFork
                }
              }
            }
          }
        }
        """
        var = {"login": request.user.username}
        hd = {"Authorization": "Bearer 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"}

        r = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': var}, headers=hd)

        g = r.json()
        dict_r = {}
        for _ in g['data']['repositoryOwner']['repositories']['edges']:
            description = [_['node']['name'], _['node']['url'], _['node']['description'],
                           _['node']['openGraphImageUrl']]
            dict_r[_['node']['name']] = description
        print(dict_r)

    return render(request, 'main.html', {'posts': posts, 'repos': dict_r}, )


# class LoginUser(LoginView):
#     form_class = blog_app.forms.LoginUserForm
#     template_name = 'login.html'
#
#     def get_success_url(self):
#         return reverse_lazy('home')


def sign_in(request):
    return render(request, 'sign_in.html')


def contact(request):
    if request.method == 'POST':
        form = forms.SendToMail(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            message = form.cleaned_data['message']
            html_for_email = render_to_string("for_email.html", {
                'email': email,
                'firstName': firstName,
                'lastName': lastName,
                'message': message,

            })

            send_mail('Contact subj', 'Hello world', '89522179992.ru@gmail.com', ['nikita76twitch.ru@gmail.com'],
                      html_message=html_for_email)
            form = forms.SendToMail()
    else:
        form = forms.SendToMail()
    return render(request, 'contact_mail.html', {'form': form}, )


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена брат")


def logout_user(request):
    logout(request)
    return redirect('home')
