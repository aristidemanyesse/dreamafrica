from django.forms import ModelForm
from .models import *

        
        
# Create the form class.
class ParticipationForm(ModelForm):
    class Meta:
        model = Participation
        fields = "__all__"
        
        
# Create the form class.
class ReservationStandForm(ModelForm):
    class Meta:
        model = ReservationStand
        fields = "__all__"
        
        
# Create the form class.
class EvenementForm(ModelForm):
    class Meta:
        model = Evenement
        fields = "__all__"
        
# Create the form class.
class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
