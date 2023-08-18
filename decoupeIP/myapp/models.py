from typing import Any
from django.db import models

#Modèle Departement qui a deux attribut nom de departement et nombre des personnes dans le departement
class Departement(models.Model):
    nomDepart = models.CharField(max_length=30)
    nbPers = models.IntegerField()
    def __str__(self):
        return f"{self.nomDepart}"

#Modèle Sous réseau qui a deux attribut address IP et masque de sous réseau
class SousReseau(models.Model):
    addressIP = models.CharField(max_length=25)
    masque = models.CharField(max_length=25)