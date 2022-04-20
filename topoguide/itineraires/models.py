from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Itineraire(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
    
    
class Sortie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    sortie_itineraire = models.ForeignKey(Itineraire,on_delete=models.CASCADE)

    