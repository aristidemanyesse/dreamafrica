from django.db import models
from django.db.models import  Q
from coreApp.models import BaseModel, Etat
from annoying.decorators import signals


class Edition(BaseModel):
    name    = models.CharField(max_length = 255, null = True, blank=True)



class TypeParticipant(BaseModel):
    name        = models.CharField(max_length = 255, null = True, blank=True)
    etiquette   = models.CharField(max_length = 255, null = True, blank=True)



class Jour(BaseModel):
    name    = models.CharField(max_length = 255, null = True, blank=True)
    edition = models.ForeignKey(Edition, on_delete = models.CASCADE, null = True, blank=True, related_name="edition_jour")


class Participant(BaseModel):
    fullname    = models.CharField(max_length = 255, default="", null = True, blank=True)
    fonction    = models.CharField(max_length = 255, default="", null = True, blank=True)
    photo       = models.ImageField(max_length = 255, upload_to = "images/participants/", default='images/participants/default.png', null = True, blank=True)
    type        = models.ForeignKey(TypeParticipant, on_delete = models.CASCADE, null = True, blank=True, related_name="type_participant")
    email       = models.EmailField(null = True, blank=True)
    contact     = models.CharField(max_length = 255, default="", null = True, blank=True)


class Actualite(BaseModel):
    titre       = models.CharField(max_length = 255, default="", null = True, blank=True)
    soustitre   = models.CharField(max_length = 255, default="", null = True, blank=True)
    auteur      = models.CharField(max_length = 255, default="", null = True, blank=True)
    debut       = models.DateTimeField(null = True, blank=True)
    fin         = models.DateTimeField(null = True, blank=True)
    code        = models.TextField(default = "")
    image        = models.ImageField(max_length = 255, upload_to = "images/actualites/", default='images/actualites/default.png', null = True, blank=True)
    edition     = models.ForeignKey(Edition, on_delete = models.CASCADE, null = True, blank=True, related_name="edition_actualite")
    
    def __str__(self):
        return self.titre
    


class Evenement(BaseModel):
    jour          = models.ForeignKey(Jour, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_produit")
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)
    time          = models.TimeField(null = True, blank=True)
    description   = models.TextField(default = "", null = True, blank=True)
    code          = models.TextField(default = "", null = True, blank=True)
    image         = models.ImageField(max_length = 255, upload_to = "images/events/", default='images/events/default.png', null = True, blank=True)
    



class CategorieStand(BaseModel):
    name          = models.CharField(max_length = 255, default="", null = True, blank=True)

class Stand(BaseModel):
    name        = models.CharField(max_length = 255, default="", null = True, blank=True)
    email       = models.EmailField(null = True, blank=True)
    contact     = models.CharField(max_length = 255, default="")
    contact2    = models.CharField(max_length = 255, default="")
    description = models.TextField(default = "")
    categorie   = models.ForeignKey(CategorieStand, on_delete = models.CASCADE, null = True, blank=True, related_name="categorie_stand")
    edition     = models.ForeignKey(Jour, on_delete = models.CASCADE, null = True, blank=True, related_name="edition_stand")
    


class Faq(BaseModel):
    question    = models.TextField(default="", null = True, blank=True)
    reponse     = models.TextField(default="", null = True, blank=True)
    
    def __str__(self):
        return self.question


@signals.pre_save(sender=Evenement)
def sighandler(instance, **kwargs):
    if instance._state.adding:
        instance.edition = Edition.objects.filter(deleted = False).order_by("created_at").last()
