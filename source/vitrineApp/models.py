from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat
from annoying.decorators import signals


class Evenement(BaseModel):
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)
    description   = models.TextField(default = "", null = True, blank=True)
    price       = models.FloatField(default= 0.0)
    edition       = models.CharField(max_length = 255, null = True, blank=True)


class Participation(BaseModel):
    fullname    = models.CharField(max_length = 255, default="", null = True, blank=True)
    email       = models.EmailField(null = True, blank=True)
    contact     = models.CharField(max_length = 255, default="", null = True, blank=True)
    description = models.TextField(default="", null = True, blank=True)
    evenement   = models.ForeignKey(Evenement, on_delete = models.CASCADE, null = True, blank=True, related_name="type_participant")
    
    def __str__(self):
        return self.fullname



class ReservationStand(BaseModel):
    fullname        = models.CharField(max_length = 255, default="", null = True, blank=True)
    email       = models.EmailField(null = True, blank=True)
    contact     = models.CharField(max_length = 255, default="")
    domaine     = models.CharField(max_length = 255, default="", null = True, blank=True)
    description = models.TextField(default = "")
    evenement   = models.ForeignKey(Evenement, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_stand")
    


class Faq(BaseModel):
    question    = models.TextField(default="", null = True, blank=True)
    reponse     = models.TextField(default="", null = True, blank=True)
    
    def __str__(self):
        return self.question

