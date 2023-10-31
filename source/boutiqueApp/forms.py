from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
        
# Create the form class.
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"



        
# Create the form class.
class UtilisateurForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
