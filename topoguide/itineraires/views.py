from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from itineraires.models import Itineraire, Sortie

from itineraires.forms import SortieForm




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

def listeSorties(request,id_itineraire):
    liste_Sorties = Sortie.objects.filter(sortie_itineraire = id_itineraire)
    print(liste_Sorties)
    context = {'liste_Sortie': liste_Sorties}
    return render(request, 'itineraires/sortie_liste.html', context)


def create_sortie(request):
    if request.method == 'GET':
        form = SortieForm()
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('itineraires:creerSortie')
    return render(request,
'itineraires/create_sortie.html', {'form': form})
    

def update_sortie(request,id_sortie):
    sortie = get_object_or_404(Sortie,pk=id_sortie)
    if request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST,instance=sortie)
        if form.is_valid():
            form.save()
        return redirect('itineraires:creerSortie')
    return render(request,
'itineraires/update_sortie.html', {'form': form})


@login_required()
def loginIndex(request):
    return HttpResponse("Connection réussie")