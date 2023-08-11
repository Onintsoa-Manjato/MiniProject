from django import forms
from .models import Departement, SousReseau

class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement

        fields = [
            "nomDepart",
            "nbPers"
        ]

class sousReseauForm(forms.ModelForm):
    class Meta:
        model = SousReseau

        fields = [
            "addressIP",
            "masque"
        ]