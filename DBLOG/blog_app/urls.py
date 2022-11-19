from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.first_page),
    path('messenger/', views.mess_page),
    path('tg_bot/', views.tgBot_page),
    path('kv_app/', views.KivyApp_page),

]
