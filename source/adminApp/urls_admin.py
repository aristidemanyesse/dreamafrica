
from django.shortcuts import redirect
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import ajax, ajax2, views

app_name = "adminApp"
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('main/dashboard/', views.dashboard, name="dashboard"),
    path('galerie/', views.galerie, name="galerie"),
    path('participants/', views.participants, name="participants"),
    
    path('blogs/', views.blogs, name="blogs"),
    path('blogs/<uuid:id>/', views.blog, name="blog"),
    path('blogs/write/<id>/', views.write_blog, name="write_blog"),
    
    path('events/', views.events, name="events"),
    
    path('stands/', views.stands, name="stands"),
    
    path('boutique/produits/', views.produits, name="produits"),
    path('boutique/commandes/', views.commandes, name="commandes"),
    path('boutique/article/new/', views.new, name="new"),
    path('boutique/article/update_produit/<uuid:id>/', views.update_produit, name="update_produit"),
    path('boutique/article/payement/stripeTokenHandler/', csrf_exempt(ajax2.stripeTokenHandler), name="stripeTokenHandler"),
    path('boutique/test/', views.test, name="test"),
    path('boutique/payement_checkout/', views.payement_checkout, name="payement_checkout"),
]