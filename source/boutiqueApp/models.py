from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat
from django.contrib.auth.models import User


class Produit(BaseModel):
    name              = models.CharField(max_length = 255, default="", null = True, blank=True)
    infos             = models.TextField(default="", null = True, blank=True)
    recettes          = models.TextField(default="", null = True, blank=True)
    avis              = models.TextField(default="", null = True, blank=True)
    faq               = models.TextField(default="", null = True, blank=True)
    price             = models.IntegerField(default = 0)
    price_reduction   = models.IntegerField(default = 0)
    description       = models.TextField(default = "", null = True, blank=True)
    image1            = models.ImageField(max_length = 255, upload_to = "images/produits/", default='images/produits/default.png', null = True, blank=True)
    image2            = models.ImageField(max_length = 255, upload_to = "images/produits/", default='images/produits/default.png', null = True, blank=True)
    image3            = models.ImageField(max_length = 255, upload_to = "images/produits/", default='images/produits/default.png', null = True, blank=True)
    image4            = models.ImageField(max_length = 255, upload_to = "images/produits/", default='images/produits/default.png', null = True, blank=True)
    
    class Meta:
        ordering = ['name']


class FaqProduit(BaseModel):
    question       = models.TextField(default = "", null = True, blank=True)
    reponse       = models.TextField(default = "", null = True, blank=True)
    produit   = models.ForeignKey(Produit, on_delete = models.CASCADE, null = True, blank=True, related_name="produit_faq")
    
    def __str__(self):
        return str(self.produit)




class Client(BaseModel):
    name    = models.CharField(max_length = 255, default="", null = True, blank=True)
    prenoms = models.CharField(max_length = 255, default="", null = True, blank=True)
    email   = models.EmailField(null = True, blank=True)
    contact = models.CharField(max_length = 255, default="", null = True, blank=True)
    adresse = models.CharField(max_length = 255, default="", null = True, blank=True)
    
    class Meta:
        ordering = ['name']



class Commande(BaseModel):
    client = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank=True, related_name="client_commande")
    price   = models.FloatField(default = 0.0, null = True, blank=True)
    client_secret   = models.TextField(default = "", null = True, blank=True)
    status   = models.BooleanField(default=False, null = True, blank=True)
        
        

class LigneCommande(BaseModel):
    produit       = models.ForeignKey(Produit, on_delete = models.CASCADE, related_name="ligne_produit")
    commande   = models.ForeignKey(Commande, on_delete = models.CASCADE, related_name="ligne_commande")
    quantite    = models.IntegerField(default = 1, null = True, blank=True)
    price   = models.FloatField(default = 0.0, null = True, blank=True)
    is_finished   = models.BooleanField(default=False, null = True, blank=True)


    def __str__(self):
        return str(self.produit) +" @ "+ str(self.commande)
