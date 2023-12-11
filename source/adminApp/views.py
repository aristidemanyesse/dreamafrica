from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from annoying.decorators import render_to
from django.http import JsonResponse

from django.core.serializers import serialize
from django.contrib.auth import authenticate, logout

from galerieApp.models import CategorieItem, Item
from boutiqueApp.models import  Commande, Produit
from vitrineApp.models import  Blog, Evenement, Participation, ReservationStand, Suggestion
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
        events = Evenement.objects.filter(deleted = False)
        produits = Produit.objects.filter(deleted = False)
        articles = Blog.objects.filter(deleted = False)
        stands = ReservationStand.objects.filter(deleted = False, created_at__date= datetime.today())
        ctx = {
            "events": events,
            "produits": produits,
            "articles": articles,
            "stands": stands,
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
          
        
        
        
@render_to('adminApp/suggestions.html')
def suggestions(request):
    if request.method == "GET":
        suggestions = Suggestion.objects.filter(deleted = False)
        ctx = {
            "suggestions": suggestions,
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
          
        
        
        
@render_to('adminApp/reservation_stands.html')
def reservations(request):
    if request.method == "GET":
        reservations = ReservationStand.objects.filter(deleted = False)
        ctx = {
            "reservations": reservations,
        }
        return ctx
          

        
@render_to('adminApp/billetterie_visiteurs.html')
def visiteurs(request):
    if request.method == "GET":
        participants = Participation.objects.filter(deleted = False)
        ctx = {
            "participants": participants,
        }
        return ctx
          

        
        
@render_to('adminApp/commandes.html')
def commandes(request):
    if request.method == "GET":
        commandes = Commande.objects.filter()
        ctx = {
            "commandes": commandes,
        }
        return ctx
          
          
             
@render_to('adminApp/commandes.html')
def valider_commande(request):
    if request.method == "POST":
        try :
            datas = request.POST
            
            Commande.objects.filter(id = datas["id"]).update(status = True)
            return JsonResponse({"status":True})

        except Exception as e:
            print("erreur save :", e)
            return JsonResponse({"status":False, "message": "Erreur lors du processus. Veuillez recommencer : "+str(e)})
    
       
        
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