from django.shortcuts import render
from annoying.decorators import render_to
from boutiqueApp.models import Categorie, Produit

# Create your views here.


@render_to('boutiqueApp/index.html')
def main(request):
    if request.method == "GET":
        categories = Categorie.objects.filter(deleted = False).order_by('name')
        produits = Produit.objects.filter(deleted = False).order_by('?')[:18]
        ctx = {
            "categories": categories,
            "produits": produits
        }
        return ctx
    
    
@render_to('boutiqueApp/categorie.html')
def categorie(request, id):
    if request.method == "GET":
        categorie = Categorie.objects.get(deleted = False, id = id)
        produits = Produit.objects.filter(deleted = False, categorie = categorie).order_by('?')[:18]
        
        ctx = {
            "categorie": categorie,
            "produits":produits
        }
        return ctx
    
    
    
@render_to('boutiqueApp/produit.html')
def produit(request, id):
    if request.method == "GET":
        produit = Produit.objects.get(deleted = False, id = id)
        produits = Produit.objects.filter(deleted = False).exclude(id = id).order_by('?')[:4]
        
        ctx = {
            "produit":produit,
            "produits":produits
        }
        return ctx
    