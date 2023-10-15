from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat



class CategorieItem(BaseModel):
    name    = models.CharField(max_length = 255, null = True, blank=True)

    class Meta:
        ordering = ['name']


class Item(BaseModel):
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)
    lieu          = models.CharField(max_length = 255, default="", null = True, blank=True)
    auteur          = models.CharField(max_length = 255, default="", null = True, blank=True)
    description   = models.TextField(default = "", null = True, blank=True)
    image        = models.ImageField(max_length = 255, upload_to = "images/galeries/", default='images/galeries/default.png', null = True, blank=True)
    categorie     = models.ForeignKey(CategorieItem, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_produit")
    
    class Meta:
        ordering = ['name']

