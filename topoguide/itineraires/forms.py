from django.forms import ModelForm
from itineraires.models import Sortie

class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = '__all__'
        
        
