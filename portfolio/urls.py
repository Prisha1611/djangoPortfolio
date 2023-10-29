from django.urls import path

from . import views
app_name = "portfolio"
urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.About, name="about"),
    path('contact/', views.Contact, name="contact"),
    path('languages/', views.Languages, name="languages"),
    path('services/', views.Services, name="services")
]