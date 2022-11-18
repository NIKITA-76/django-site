from django.shortcuts import render


def first_page(request):
    return render(request, 'first_page.html')


def mess_page(request):
    return render(request, 'messenger_page.html')


def tgBot_page(request):
    return render(request, 'tgBot_page.html')


def KivyApp_page(request):
    return render(request, 'KivyApp_page.html')
