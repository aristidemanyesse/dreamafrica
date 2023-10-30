from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
import json
from django.core.serializers import serialize
from django.contrib.auth import authenticate, logout

from galerieApp.models import CategorieItem, Item
from boutiqueApp.models import  Produit
from vitrineApp.models import  Blog, Evenement, Participation, ReservationStand
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
        return {}
        


def deconnexion(request):
    if request.method == "GET":
        return redirect("authApp:login") 
        
        
        
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
        
        
        
        
@render_to('adminApp/blogs.html')
def blogs(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(deleted = False)
        ctx = {
            "blogs": blogs,
        }
        return ctx
        
@render_to('adminApp/blog.html')
def blog(request, id):
    if request.method == "GET":
        blog = get_object_or_404(Blog, id = id, deleted = False)
        ctx = {
            "blog": blog,
        }
        return ctx
    
    
@render_to('adminApp/write_blog.html')
def write_blog(request, id):
    if request.method == "GET":
        if id == "new":
            ctx = {}
        else:
            blogs = Blog.objects.filter(id=id)
            ctx = {
                "blog": blogs.first
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
        ctx = {
            "events": events,
        }
        return ctx
          
        
        
        
@render_to('adminApp/stands.html')
def stands(request):
    if request.method == "GET":
        participants = Participation.objects.filter(deleted = False)
        ctx = {
            "participants": participants,
        }
        return ctx
          

        
        
@render_to('adminApp/commandes.html')
def commandes(request):
    if request.method == "GET":
        # types = TypeParticipant.objects.filter(deleted = False)
        # participants = Participant.objects.filter(deleted = False)
        ctx = {
            # "types": types,
            # "participants": participants,
            # "officinedemandes": demandes,
        }
        return ctx
          
          
        
        
@render_to('adminApp/produits.html')
def produits(request):
    if request.method == "GET":
        produits = Produit.objects.filter(deleted = False)
        ctx = {
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
          

        
@render_to('adminApp/payement_checkout.html')
def payement_checkout(request):
    if request.method == "GET":
        datas = request.GET
        participation = Participation.objects.get(client_secret = datas["payment_intent_client_secret"])
        
        participation.payement_intent = datas["payment_intent"]
        participation.status = datas["redirect_status"] == "succeeded"
        participation.save()
        
        ctx = {
            "test": "test",
        }
        return ctx