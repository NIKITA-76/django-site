from django.urls import path
from blog_app import views

urlpatterns = [
    path('', views.first_page),
    path('contact_to_mail/', views.contact, name="contact"),

]
