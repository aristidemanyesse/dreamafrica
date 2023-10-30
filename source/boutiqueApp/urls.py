from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views, ajax

app_name = "boutiqueApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('produit/<uuid:id>/', views.produit, name='produit'),
    path('panier/', views.panier, name='panier'),
    path('payement/stripeTokenHandler/', csrf_exempt(ajax.stripeTokenHandler), name="stripeTokenHandler"),
]