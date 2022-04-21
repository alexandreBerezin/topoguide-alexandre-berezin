from django.forms import ModelForm
from itineraires.models import Sortie

class SortieForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ['sortie_itineraire','date',
                  'duree_reelle','nombre_personnes',
                  'groupe_experience','meteo',
                  'difficulte_ressentie']
        
        
