
from django.shortcuts import redirect
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import ajax, ajax2, views

app_name = "authApp"
urlpatterns = [
   
    path('login/', views.connexion, name="login"),
    path('locked', views.locked, name="locked"),
    path('logout/', views.deconnexion, name="logout"),
    
    path('ajax/connexion/', ajax.connexion),
    path('ajax/first_user/', ajax.first_user),
    path('ajax/unlocked/', ajax.unlocked),
    path('ajax/forgetpassword/', ajax.forgetpassword),
    path('ajax/reset/', ajax.reset),
]