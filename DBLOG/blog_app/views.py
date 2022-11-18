from django.shortcuts import render


def first_page(request):
    return render(request, 'first_page.html')


def mess_page(request):
    return render(request, 'messenger_page.html')
