from django.urls import path

from . import views

app_name = "boutiqueApp"
urlpatterns = [
    path('', views.main, name='main'),
    path('produit/<uuid:id>/', views.produit, name='produit'),
    path('panier/', views.panier, name='panier'),
]