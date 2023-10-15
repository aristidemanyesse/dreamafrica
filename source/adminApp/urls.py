
from django.shortcuts import redirect
from django.urls import path

from . import views, ajax

app_name = "adminApp"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('main/dashboard', views.dashboard, name="dashboard"),
    path('galerie/', views.galerie, name="galerie"),
    path('participants/', views.participants, name="participants"),
    
    path('actualites/', views.actualites, name="actualites"),
    path('actualites/<uuid:id>/', views.actualite, name="actualite"),
    
    path('events/', views.events, name="events"),
    
    path('stands/', views.stands, name="stands"),
    
    path('boutique/produits/', views.produits, name="produits"),
    path('boutique/commandes/', views.commandes, name="commandes"),
    path('boutique/article/new/', views.new, name="new"),
    path('boutique/article/update_produit/<uuid:id>/', views.update_produit, name="update_produit"),
    path('boutique/article/payement/stripeTokenHandler/', ajax.stripeTokenHandler, name="stripeTokenHandler"),
    path('boutique/test/', views.test, name="test"),
    path('boutique/payement_checkout/', views.payement_checkout, name="payement_checkout"),
    
    
    path('login/', views.connexion, name="login"),
    path('locked', views.locked, name="locked"),
    path('logout/', views.deconnexion, name="logout"),
   
    
    # path('auth/ajax/connexion/', ajax.connexion),
    # path('auth/ajax/first_user/', ajax.first_user),
    # path('auth/ajax/unlocked/', ajax.unlocked),
    # path('auth/ajax/forgetpassword/', ajax.forgetpassword),
    # path('auth/ajax/reset/', ajax.reset),
    
    # path('main/dashboard/ajouter/', ajax2.ajouter),
    # path('main/dashboard/check_demande/', ajax2.check_demande),
    # path('main/dashboard/valider_demande/', ajax2.valider_demande),
]