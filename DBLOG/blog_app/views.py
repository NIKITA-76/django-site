from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from blog_app import models
from blog_app import forms

import blog_app


class BlogHome(ListView):
    model = models.ModelPost
    template_name = 'main.html'
    context_object_name = 'posts'


class LoginUser(LoginView):
    form_class = blog_app.forms.LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


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
