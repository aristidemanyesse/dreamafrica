from django.shortcuts import render
from annoying.decorators import render_to
from settings.settings import BASE_DIR
from boutiqueApp.models import Produit
from vitrineApp.models import Faq
import os, random
# Create your views here.


@render_to('vitrineApp/index.html')
def main(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    

@render_to('vitrineApp/mna.html')
def mna(request):
    fichiers = []
    dossier = os.path.join(BASE_DIR, "static/images/mna/")
    liste_fichiers = os.listdir(dossier)
    for fichier in liste_fichiers:
        chemin_complet = os.path.join(dossier, fichier)  # Obtenez le chemin complet du fichier
        if os.path.isfile(chemin_complet):  # Vérifiez si c'est un fichier (pas un dossier)
            fichiers.append(os.path.join("images/mna/", fichier))
    random.shuffle(fichiers)
    produits = Produit.objects.filter(deleted = False).order_by('?')[:4]
    if request.method == "GET":
        ctx = {
            "fichiers": fichiers,
            "produits": produits,
        }
        return ctx
    
    

@render_to('vitrineApp/fap.html')
def fap(request):
    fichiers = []
    dossier = os.path.join(BASE_DIR, "static/images/fap/")
    liste_fichiers = os.listdir(dossier)
    for fichier in liste_fichiers:
        chemin_complet = os.path.join(dossier, fichier)  # Obtenez le chemin complet du fichier
        if os.path.isfile(chemin_complet):  # Vérifiez si c'est un fichier (pas un dossier)
            fichiers.append(os.path.join("images/fap/", fichier))
    random.shuffle(fichiers)
    produits = Produit.objects.filter(deleted = False).order_by('?')[:4]
    if request.method == "GET":
        ctx = {
            "fichiers": fichiers,
            "produits": produits,
        }
        return ctx
    

@render_to('vitrineApp/afc.html')
def afc(request):
    fichiers = []
    dossier = os.path.join(BASE_DIR, "static/images/afc/")
    liste_fichiers = os.listdir(dossier)
    for fichier in liste_fichiers:
        chemin_complet = os.path.join(dossier, fichier)  # Obtenez le chemin complet du fichier
        if os.path.isfile(chemin_complet):  # Vérifiez si c'est un fichier (pas un dossier)
            fichiers.append(os.path.join("images/afc/", fichier))
    random.shuffle(fichiers)
    produits = Produit.objects.filter(deleted = False).order_by('?')[:4]
    if request.method == "GET":
        ctx = {
            "fichiers": fichiers,
            "produits": produits,
        }
        return ctx
    
    

@render_to('vitrineApp/fwa.html')
def fwa(request):
    fichiers = []
    dossier = os.path.join(BASE_DIR, "static/images/fwa/")
    liste_fichiers = os.listdir(dossier)
    for fichier in liste_fichiers:
        chemin_complet = os.path.join(dossier, fichier)  # Obtenez le chemin complet du fichier
        if os.path.isfile(chemin_complet):  # Vérifiez si c'est un fichier (pas un dossier)
            fichiers.append(os.path.join("images/fwa/", fichier))
    random.shuffle(fichiers)
    produits = Produit.objects.filter(deleted = False).order_by('?')[:4]
    if request.method == "GET":
        ctx = {
            "fichiers": fichiers,
            "produits": produits,
        }
        return ctx
    
    
@render_to('vitrineApp/billetterie.html')
def billetterie(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
    
@render_to('vitrineApp/faq.html')
def faq(request):
    if request.method == "GET":
        faqs = Faq.objects.all()
        ctx = {
            "faqs": faqs
        }
        return ctx
    
    
@render_to('vitrineApp/juste.html')
def juste(request):
    fichiers = []
    dossier = os.path.join(BASE_DIR, "static/images/juste/")
    liste_fichiers = os.listdir(dossier)
    for fichier in liste_fichiers:
        chemin_complet = os.path.join(dossier, fichier)  # Obtenez le chemin complet du fichier
        if os.path.isfile(chemin_complet):  # Vérifiez si c'est un fichier (pas un dossier)
            fichiers.append(os.path.join("images/juste/", fichier))
    random.shuffle(fichiers)
    produits = Produit.objects.filter(deleted = False).order_by('?')[:4]
    if request.method == "GET":
        ctx = {
            "fichiers": fichiers,
            "produits": produits,
        }
        return ctx
    
    
    
@render_to('vitrineApp/participants.html')
def fica(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
@render_to('vitrineApp/stand.html')
def stand(request):
    if request.method == "GET":
        ctx = {}
        return ctx
    
    
# @render_to('vitrineApp/unes.html')
# def unes(request):
#     if request.method == "GET":
#         ctx = {}
#         return ctx
    
    
@render_to('vitrineApp/contacts.html')
def contacts(request):
    if request.method == "GET":
        ctx = {}
        return ctx