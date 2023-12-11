import json
from annoying.decorators import render_to
from boutiqueApp.models import Commande, LigneCommande, Produit
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout, login

from coreApp.models import Etat
# Create your views here.


@render_to('boutiqueApp/index.html')
def main(request):
    if request.method == "GET":
        produits = Produit.objects.filter(deleted = False)
        ctx = {
            "produits": produits
        }
        return ctx
    


@render_to('boutiqueApp/acompte.html')
def acompte(request):
    if request.method == "GET":
        if not request.user.is_authenticated:
            return redirect("boutiqueApp:main") 
        
        attentes = Commande.objects.filter(client = request.user, status = False)
        finis = Commande.objects.filter(client = request.user, status = True, deleted = False)
        ctx = {
            "attentes": attentes,
            "finis": finis,
        }
        return ctx
    



def deconnexion(request):
    if request.method == "GET":
        logout(request)
        if 'locked' in request.session:
            del request.session['locked']
        return redirect("boutiqueApp:main") 
    
    
    
    
@render_to('boutiqueApp/panier.html')
def panier(request):
    if request.method == "GET":
        total = 0
        panier = json.loads(request.session.get("dreamteam-panier", "[]"))
        produits = Produit.objects.filter(deleted = False, id__in = [key for key in panier]) if panier is not None else []
        lignes = []
        for prod in produits:
            total += prod.price * panier[str(prod.id)]
            lignes.append(
                LigneCommande(
                    produit = prod,
                    quantite = panier[str(prod.id)]
                )
            )
            
        produits = Produit.objects.filter(deleted = False)[:4]
        ctx = {
            "total":total,
            "lignes":lignes,
            "produits":produits,
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



@render_to('boutiqueApp/payement_commande.html')
def payement_commande(request, id):
    if request.method == "GET":
        commande = Commande.objects.get(id = id)
        ctx = {
            "commande": commande,
        }
        return ctx