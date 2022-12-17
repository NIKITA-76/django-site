from django.urls import path, include
from blog_app import views

urlpatterns = [
    path('', views.first_page, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('contact_to_mail/', views.contact, name="contact"),
    path('project_about/', views.project_about, name="prj_abt"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('social-auth/', include('social_django.urls', namespace='social'))

]