
from django.shortcuts import redirect
from django.urls import path

from . import ajax, views

app_name = "adminApp"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('main/dashboard/', views.dashboard, name="dashboard"),
    path('galerie/', views.galerie, name="galerie"),
    
    path('blogs/', views.blogs, name="blogs"),
    path('blogs/<uuid:id>/', views.blog, name="blog"),
    path('blogs/write/<id>/', views.write_blog, name="write_blog"),
    
    path('events/', views.events, name="events"),
    
    path('billetterie_visiteurs/', views.visiteurs, name="billetterie_visiteurs"),
    path('reservation_stands/', views.reservations, name="reservation_stands"),
    
    path('suggestions/', views.suggestions, name="suggestions"),
    
    path('boutique/produits/', views.produits, name="produits"),
    path('boutique/commandes/', views.commandes, name="commandes"),
    path('boutique/commandes/valider/', views.valider_commande, name="valider_commande"),
    path('boutique/article/new/', views.new, name="new"),
    path('boutique/article/update_produit/<uuid:id>/', views.update_produit, name="update_produit"),
    path('boutique/test/', views.test, name="test"),
    path('boutique/payement_checkout/', views.payement_checkout, name="payement_checkout"),
]