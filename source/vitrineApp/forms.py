from django.forms import ModelForm
from .models import *

        
# Create the form class.
class TypeParticipantForm(ModelForm):
    class Meta:
        model = TypeParticipant
        fields = "__all__"
        
        
# Create the form class.
class ParticipantForm(ModelForm):
    class Meta:
        model = Participant
        fields = "__all__"
        
        
# Create the form class.
class ActualiteForm(ModelForm):
    class Meta:
        model = Actualite
        fields = "__all__"
        
        
# Create the form class.
class EvenementForm(ModelForm):
    class Meta:
        model = Evenement
        fields = "__all__"
