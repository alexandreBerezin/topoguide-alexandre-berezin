from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from itineraires.models import Itineraire


def index(request):
    return HttpResponse("Index de l'application itineraires: pour se connecteur cliquer ici : ")

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponse("Déconnection réussie")


def listeItineraires(request):
    liste_Itineraires = Itineraire.objects.all()
    context = {'liste_Itineraires': liste_Itineraires}
    return render(request, 'itineraires/itineraires_liste.html', context)


@login_required()
def loginIndex(request):
    return HttpResponse("Connection réussie")