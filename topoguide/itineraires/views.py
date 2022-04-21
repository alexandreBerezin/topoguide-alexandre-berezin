from django.shortcuts import get_object_or_404, redirect, render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout

from itineraires.models import Itineraire, Sortie

from itineraires.forms import SortieForm





#Définition de la vue index qui va être appellée en premier
# Cette vue contient un bouton pour se connecter à l'application
def index(request):
    context = {}
    return render(request, 'itineraires/index.html', context)


#Définirion de la vue de logout
def logout_view(request):
    logout(request)
    # Redirect jusqu'a l'index
    return redirect('index')


#utilisation de login requiered pour toutes les vues en dessous (partie authentifiée du site)
@login_required()
#Cette page renvoie une liste des tous les itinéaires avec la possibilité de clique sur chaque pour avoir le détail
def listeItineraires(request):
    username = request.user.username
    liste_Itineraires = Itineraire.objects.all()
    context = {'liste_Itineraires': liste_Itineraires, 'username': username}
    return render(request, 'itineraires/itineraires_liste.html', context)


#Cette vue afficher la liste des sorties correspondant à un itinéraire précis et décrit 
# ce même itinéaire
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


#une vue qui créer une sortie pour l'utilisateur courant
@login_required()
def create_sortie(request):
    #on récupére les données de request
    username = request.user.username
    #On préremplie un modèle avec l'utilisateur courant comme user
    sortie_pre = Sortie(user = request.user )
    if request.method == 'GET':
        form = SortieForm(instance =sortie_pre )
    elif request.method == 'POST':
        form = SortieForm(request.POST,instance=sortie_pre)
        if form.is_valid():
            form.save()
        else:
            print("FORM NON VALIDE")
            print (form.errors)
            #Si le form n'est pas valide on affiche l'erreur
            return HttpResponse('Error dans le form ' + str(form.errors))
        return redirect('itineraires:creerSortie')
    return render(request,
'itineraires/create_sortie.html', {'form': form,'username': username})
    
    
#Vue qui modifie une Sortie
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

#Vue qui affiche toutes les sorties de l'utilisateur courant
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

#Vue qui afiche les détails d'une sortie 
@login_required()
def detail_sortie(request,id_sortie):
    username = request.user.username
    sortie = get_object_or_404(Sortie,pk=id_sortie)
    print(sortie.sortie_itineraire.id)
    itineraire = get_object_or_404(Itineraire,pk=sortie.sortie_itineraire.id)
    context = {'sortie' : sortie,
               'itineraire' : itineraire,
               'username': username}
    return render(request,'itineraires/detail_sortie.html', context)