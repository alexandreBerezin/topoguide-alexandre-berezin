from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('loginIndex', views.loginIndex, name='loginIndex'),
    path('logout', views.logout_view, name='logout'),
    path('itinerairesList', views.listeItineraires, name='itinerairesList'),
    path('sorties/<int:id_itineraire>', views.listeSorties, name='vueSortie'),
]