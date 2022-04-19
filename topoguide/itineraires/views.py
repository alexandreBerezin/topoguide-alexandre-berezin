from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout


def index(request):
    return HttpResponse("Index de l'application itineraires: pour se connecteur cliquer ici : ")

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponse("Déconnection réussie")


@login_required()
def loginIndex(request):
    return HttpResponse("Connection réussie")