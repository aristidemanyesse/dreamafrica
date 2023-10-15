from django.forms import ModelForm
from .models import *

        
# Create the form class.
class CategorieItemForm(ModelForm):
    class Meta:
        model = CategorieItem
        fields = "__all__"
        
        
# Create the form class.
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"
