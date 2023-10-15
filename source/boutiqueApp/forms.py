from django.forms import ModelForm
from .models import *

        
# Create the form class.
class CategorieForm(ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"
        
        
# Create the form class.
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
