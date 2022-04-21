from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from itineraires.models import Itineraire, Sortie

from itineraires.forms import SortieForm






def index(request):
    context = {}
    return render(request, 'itineraires/index.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('index')

@login_required()
def listeItineraires(request):
    username = request.user.username
    liste_Itineraires = Itineraire.objects.all()
    context = {'liste_Itineraires': liste_Itineraires, 'username': username}
    return render(request, 'itineraires/itineraires_liste.html', context)

@login_required()
def listeSorties(request,id_itineraire):
    
    username = request.user.username
    itineraire = get_object_or_404(Itineraire,pk=id_itineraire)
    liste_Sorties = Sortie.objects.filter(sortie_itineraire = id_itineraire)
    print(liste_Sorties)
    context = {'liste_Sortie': liste_Sorties,
               'itineraire' : itineraire,
               'username': username}
    return render(request, 'itineraires/sortie_liste.html', context)

@login_required()
def create_sortie(request):
    username = request.user.username
    if request.method == 'GET':
        form = SortieForm()
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('itineraires:creerSortie')
    return render(request,
'itineraires/create_sortie.html', {'form': form,'username': username})
    
@login_required()
def update_sortie(request,id_sortie):
    username = request.user.username
    sortie = get_object_or_404(Sortie,pk=id_sortie)
    if request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST,instance=sortie)
        if form.is_valid():
            form.save()
        return redirect('itineraires:mesSorties')
    return render(request,
'itineraires/update_sortie.html', {'form': form,'username': username})


@login_required()
def mySorties(request):
    username = request.user.username
    current_user = request.user
    liste_Sorties = Sortie.objects.filter( user = current_user.id)
    context = {'id': current_user.id,
               'liste_Sortie' : liste_Sorties,
               'username': username}
    
    return render(request,'itineraires/mySorties.html', context)


@login_required()
def loginIndex(request):
    return HttpResponse("Connection réussie")

def detail_sortie(request,id_sortie):
    username = request.user.username
    sortie = get_object_or_404(Sortie,pk=id_sortie)
    print(sortie.sortie_itineraire.id)
    itineraire = get_object_or_404(Itineraire,pk=sortie.sortie_itineraire.id)
    context = {'sortie' : sortie,
               'itineraire' : itineraire,
               'username': username}
    return render(request,'itineraires/detail_sortie.html', context)