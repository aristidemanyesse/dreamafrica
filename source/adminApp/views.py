from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
import json
from django.core.serializers import serialize
from django.contrib.auth import authenticate, logout

from galerieApp.models import CategorieItem, Item
from boutiqueApp.models import Categorie, Produit
from vitrineApp.models import Actualite, Evenement, Jour, Participant, Stand, TypeParticipant
from .models import *
from datetime import datetime, timedelta
# Create your views here.



        

@render_to('adminApp/login.html')
def connexion(request):
    if request.method == "GET":
        logout(request)
        if 'locked' in request.session:
            del request.session['locked']
            
        return {}
        
        

@render_to('adminApp/locked.html')
def locked(request):
    if request.method == "GET":
        request.session['locked'] = True
        if "last_url" not in request.session:
            request.session['last_url'] = request.META["HTTP_REFERER"]
        return render(request, "auth/pages/locked.html")
        


def deconnexion(request):
    if request.method == "GET":
        return redirect("adminApp:login") 
        
        
        
@render_to('adminApp/dashboard.html')
def dashboard(request):
    if not request.user.is_superuser:
        pass
        # return redirect("adminApp:dashboard_officine", request.officine.id)
        
    if request.method == "GET":
        # officines = Officine.objects.filter(deleted = False, type  = TypeOfficine.objects.get(etiquette = TypeOfficine.PHARMACIE))
        # markers = json.loads(serialize("geojson", officines))
        # produits = Produit.objects.filter(deleted = False, type = TypeProduit.objects.get(etiquette = TypeProduit.MEDICAMENT))
        # users = Utilisateur.objects.filter(deleted = False)
        # demandes = Demande.objects.filter(deleted = False, created_at__date= datetime.today())
        ctx = {
            # "officines": officines,
            # # "produits": produits,
            # # "users": users,
            # # "demandes": demandes,
            # "markers": markers
        }
        return ctx
        



        
@render_to('adminApp/galerie.html')
def galerie(request):
    if request.method == "GET":
        categories = CategorieItem.objects.filter(deleted = False)
        items = Item.objects.filter(deleted = False)
        ctx = {
            "categories": categories,
            "items": items,
            # "officinedemandes": demandes,
        }
        return ctx
          
        
        
@render_to('adminApp/participants.html')
def participants(request):
    if request.method == "GET":
        types = TypeParticipant.objects.filter(deleted = False)
        participants = Participant.objects.filter(deleted = False)
        ctx = {
            "types": types,
            "participants": participants,
        }
        return ctx
        
        
        
        
@render_to('adminApp/actualites.html')
def actualites(request):
    if request.method == "GET":
        actualites = Actualite.objects.filter(deleted = False)
        ctx = {
            "actualites": actualites,
        }
        return ctx
        
@render_to('adminApp/actualite.html')
def actualite(request, id):
    if request.method == "GET":
        actualite = get_object_or_404(Actualite, id = id, deleted = False)
        ctx = {
            "actualite": actualite,
        }
        return ctx
    
    
    
@render_to('adminApp/write.html')
def new(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('adminApp/update_produit.html')
def update_produit(request, id):
    if request.method == "GET":
        produit = get_object_or_404(Produit, id = id, deleted = False)
        ctx = {
            "produit": produit
        }
        return ctx
          
        
        
        
@render_to('adminApp/events.html')
def events(request):
    if request.method == "GET":
        events = Evenement.objects.filter(deleted = False)
        jours = Jour.objects.filter(deleted = False)
        ctx = {
            "events": events,
            "jours": jours,
        }
        return ctx
          
        
        
        
@render_to('adminApp/stands.html')
def stands(request):
    if request.method == "GET":
        stands = Stand.objects.filter(deleted = False)
        ctx = {
            "stands": stands,
        }
        return ctx
          

        
        
@render_to('adminApp/commandes.html')
def commandes(request):
    if request.method == "GET":
        types = TypeParticipant.objects.filter(deleted = False)
        participants = Participant.objects.filter(deleted = False)
        ctx = {
            "types": types,
            "participants": participants,
            # "officinedemandes": demandes,
        }
        return ctx
          
          
        
        
@render_to('adminApp/produits.html')
def produits(request):
    if request.method == "GET":
        categories = Categorie.objects.filter(deleted = False)
        produits = Produit.objects.filter(deleted = False)
        ctx = {
            "categories": categories,
            "produits": produits,
        }
        return ctx
          
          
          

        
@render_to('adminApp/test.html')
def test(request):
    if request.method == "GET":
        ctx = {
            "test": "test",
        }
        return ctx
          

        
# @render_to('adminApp/payement_checkout.html')
def payement_checkout(request):
    if request.method == "POST":
        print(request.POST)
        ctx = {
            "test": "test",
        }
        return ctx