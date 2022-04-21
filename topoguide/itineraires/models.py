from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Itineraire(models.Model):
    title = models.CharField(max_length=200)
    start = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    altitude_start = models.IntegerField()
    altitude_min = models.IntegerField()
    altitude_max = models.IntegerField()
    
    denivele_positif = models.IntegerField()
    denivele_negatif = models.IntegerField()
    duree_estimee = models.FloatField()
    difficulte = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    
    
class Sortie(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sortie_itineraire = models.ForeignKey(Itineraire,on_delete=models.CASCADE)
    date = models.DateTimeField()
    duree_reelle = models.FloatField()
    nombre_personnes = models.IntegerField()
    groupe_experience = models.IntegerField()
    meteo = models.CharField(max_length=200)
    difficulte_ressentie = models.IntegerField()

    
    def __str__(self):

        return self.user.username + " " +  self.sortie_itineraire.title + " " + str(self.date)[:10]
    
    
    
    

    