from django.urls import path

from . import views

app_name = "galerieApp"
urlpatterns = [
    path('', views.main, name='main'),
]