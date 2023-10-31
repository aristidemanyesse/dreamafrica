from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views, ajax

app_name = "boutiqueApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('produit/<uuid:id>/', views.produit, name='produit'),
    path('panier/', views.panier, name='panier'),
    
    path('panier_price/', csrf_exempt(ajax.panier_price), name="panier_price"),
    path('payement/stripeTokenHandler/', csrf_exempt(ajax.stripeTokenHandler), name="stripeTokenHandler"),
    path('connexion/', csrf_exempt(ajax.connexion), name="connexion"),
    path('inscription/', csrf_exempt(ajax.inscription), name="inscription"),
]