from django.urls import path

from . import views

app_name = 'itineraires'

urlpatterns = [
    path('', views.index, name='index'),
    path('loginIndex', views.loginIndex, name='loginIndex'),
    path('logout', views.logout_view, name='logout'),
    path('itinerairesList', views.listeItineraires, name='itinerairesList'),
    path('sorties/<int:id_itineraire>', views.listeSorties, name='vueSortie'),
    path('sorties/create', views.create_sortie, name='creerSortie'),
    path('sorties/update/<int:id_sortie>', views.update_sortie, name='modifierSortie'),
    path('sorties/mySorties', views.mySorties, name='mesSorties'),
]