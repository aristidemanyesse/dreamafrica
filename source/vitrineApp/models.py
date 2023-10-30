from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat
from annoying.decorators import signals
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

class Evenement(BaseModel):
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)
    description   = models.TextField(default = "", null = True, blank=True)
    price       = models.FloatField(default= 0.0)
    edition       = models.CharField(max_length = 255, null = True, blank=True)


class Participation(BaseModel):
    fullname          = models.CharField(max_length = 255, default="", null = True, blank=True)
    email             = models.EmailField(null = True, blank=True)
    quantite          = models.IntegerField(default=1, null = True, blank=True)
    contact           = models.CharField(max_length = 255, default="", null = True, blank=True)
    description       = models.TextField(default="", null = True, blank=True)
    evenement         = models.ForeignKey(Evenement, on_delete = models.CASCADE, null = True, blank=True, related_name="type_participant")
    price             = models.TextField(default="", null = True, blank=True)
    payement_intent   = models.TextField(default="", null = True, blank=True)
    client_secret     = models.TextField(default="", null = True, blank=True)
    status            = models.BooleanField(default=False)
    
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


class Blog(BaseModel):
    title       = models.TextField(default="", null = True, blank=True)
    subtitle    = models.TextField(default="", null = True, blank=True)
    content     = models.TextField(default="", null = True, blank=True)
    image       = models.ImageField(max_length = 255, upload_to = "images/blogs/", default='images/blogs/default.png', null = True, blank=True)

    
    def __str__(self):
        return self.title
    
    
    
    


@receiver(pre_save, sender=Participation)
def _(sender, instance, **kwargs):
    instance.price = instance.quantite * instance.evenement.price
    