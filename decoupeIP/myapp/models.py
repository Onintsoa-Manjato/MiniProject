from typing import Any
from django.db import models

class Departement(models.Model):
    nomDepart = models.CharField(max_length=30)
    nbPers = models.IntegerField()
    def __str__(self):
        return self.nomDepart

class SousReseau(models.Model):
    addressIP = models.CharField(max_length=25)
    masque = models.CharField(max_length=25)