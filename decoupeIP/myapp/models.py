from typing import Any
from django.db import models

class Departement(models.Model):
    nomDepart = models.CharField(max_length=30)
    nbPers = models.IntegerField()

class SousReseau(models.Model):
    addressIP = models.CharField(max_length=25)
    masque = models.CharField(max_length=25)

class PlageAdress(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    sousReseau = models.ManyToManyField(SousReseau)
    adresseDiffus = models.CharField(max_length=25)
    nbHote = models.IntegerField()
