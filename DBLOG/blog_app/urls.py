from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name="home"),
    path('contact_to_mail/', views.contact, name="contact"),
    path('sign_in/', views.sign_in, name="sign_in"),

]
