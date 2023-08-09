from django.contrib import admin
from .models import Departement, SousReseau, PlageAdress

class DepartementAdmin(admin.ModelAdmin):
    list_display = ("nomDepart", "nbPers")

class SousReseauAdmin(admin.ModelAdmin):
    list_display = ("addressIP", "masque")

class PlageAdressAdmin(admin.ModelAdmin):
    list_display = ("adresseDiffus", "nbHote")

admin.site.register(Departement, DepartementAdmin)
admin.site.register(SousReseau, SousReseauAdmin)
admin.site.register(PlageAdress, PlageAdressAdmin)