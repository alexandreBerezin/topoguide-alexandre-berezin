from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Index de l'application itineraires: pour se connecteur cliquer ici : ")
