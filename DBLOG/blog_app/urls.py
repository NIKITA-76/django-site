from django.urls import path, include
from blog_app import views

urlpatterns = [
    path('', views.first_page, name="home"),
    #path('login/', views.LoginUser.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('contact_to_mail/', views.contact, name="contact"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('social-auth/', include('social_django.urls', namespace='social'))

]