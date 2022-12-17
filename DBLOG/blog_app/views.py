from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.core.mail import send_mail
from django.template.loader import render_to_string
from blog_app import forms

import requests


def first_page(request):
    print(request)
    description = []
    description_user = []
    dict_r = {}
    if request.user.is_authenticated:
        query = """
        query ($login: String!, $login_avtr: String!) {
  repositoryOwner(login: $login) {
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
          createdAt
        }
      }
    }
  }
  user(login: $login_avtr) {
    createdAt
    followers {
      totalCount
    }
    name
    avatarUrl
    bio
  }
}
        """
        var = {
            "login": request.user.username,
            "login_avtr": request.user.username
        }
        hd = {"Authorization": "Bearer "}

        r = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': var}, headers=hd)

        g = r.json()
        print(g)
        for k, i in g['data']['user'].items():
            if type(i) == dict:
                description_user.append(i['totalCount'])
                continue
            description_user.append(i)

        for date in g['data']['repositoryOwner']['repositories']['edges']:
            description = [date['node']['name'], date['node']['url'], date['node']['description'],
                           date['node']['openGraphImageUrl'],
                           date['node']['createdAt']]
            dict_r[date['node']['name']] = description
        print(dict_r)
        print(description_user)

    return render(request, 'main.html', {'user': description_user, 'repos': dict_r}, )


def sign_in(request):
    return render(request, 'sign_in.html')


def project_about(request):
    return render(request, 'project_about.html')


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
