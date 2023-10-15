from django.contrib import admin

# Register your models here.
from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat



class Parametre(BaseModel):
    email           = models.EmailField(max_length = 255, null = True, blank=True)
    localisation    = models.CharField(max_length = 255, null = True, blank=True)
    contacts        = models.CharField(max_length = 255, null = True, blank=True)



class Newletter(BaseModel):
    email   = models.EmailField(null = True, blank=True)
    enable   = models.BooleanField(default=True)