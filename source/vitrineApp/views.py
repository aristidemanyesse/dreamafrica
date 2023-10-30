from django.shortcuts import render, redirect
from annoying.decorators import render_to
from settings.settings import BASE_DIR
from boutiqueApp.models import Produit
from vitrineApp.models import Blog, Evenement, Faq, Participation
import os, random
# Create your views here.


@render_to('vitrineApp/index.html')
def index(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(deleted = False)[:3]
        events =  Evenement.objects.filter(deleted = False)
        ctx = {
            "blogs": blogs,
            "events": events,
        }
        return ctx
    
    

@render_to('vitrineApp/mna.html')
def mna(request):
    events =  Evenement.objects.filter(deleted = False)
    if request.method == "GET":
        ctx = {
            "events": events,
        }
        return ctx
    
    

@render_to('vitrineApp/fap.html')
def fap(request):
    events =  Evenement.objects.filter(deleted = False)
    if request.method == "GET":
        ctx = {
            "events": events,
        }
        return ctx
    

@render_to('vitrineApp/afc.html')
def afc(request):
    events =  Evenement.objects.filter(deleted = False)
    if request.method == "GET":
        ctx = {
            "events": events,
        }
        return ctx
    
    

@render_to('vitrineApp/fwa.html')
def fwa(request):
    events =  Evenement.objects.filter(deleted = False)
    blogs = Blog.objects.filter(deleted = False)[:3]
    if request.method == "GET":
        ctx = {
            "blogs": blogs,
            "events": events,
        }
        return ctx
    
    
@render_to('vitrineApp/billetterie.html')
def billetterie(request):
    if request.method == "GET":
        events =  Evenement.objects.filter(deleted = False)
        ctx = {
            "events":events,
        }
        return ctx
    
    
    
@render_to('vitrineApp/juste.html')
def juste(request):
    events =  Evenement.objects.filter(deleted = False)
    if request.method == "GET":
        ctx = {
            "events": events,
        }
        return ctx
    
    
    
@render_to('vitrineApp/fica.html')
def fica(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(deleted = False)[:3]
        events =  Evenement.objects.filter(deleted = False)
        ctx = {
            "events":events,
            "blogs":blogs,
        }
        return ctx
    



@render_to('vitrineApp/stand.html')
def stand(request):
    if request.method == "GET":
        events =  Evenement.objects.filter(deleted = False)
        ctx = {
            "events": events
        }
        return ctx
    
    
@render_to('vitrineApp/purchase.html')
def purchase(request, id):
    if request.method == "GET":
        participation = Participation.objects.get(id = id)
        ctx = {
            "participation": participation,
        }
        return ctx


@render_to('vitrineApp/blogs.html')
def blogs(request):
    if request.method == "GET":
        blogs = Blog.objects.filter(deleted = False)
        events =  Evenement.objects.filter(deleted = False)
        ctx = {
            "blogs": blogs,
            "events": events,
        }
        return ctx


@render_to('vitrineApp/blog.html')
def blog(request, id):
    if request.method == "GET":
        blog = Blog.objects.get(id = id)
        ctx = {
            "blog": blog
        }
        return ctx
    
    
@render_to('vitrineApp/contacts.html')
def contacts(request):
    if request.method == "GET":
        ctx = {}
        return ctx