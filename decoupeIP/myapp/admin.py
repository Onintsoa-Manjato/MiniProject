from django.contrib import admin
from .models import Departement, SousReseau

class DepartementAdmin(admin.ModelAdmin):
    list_display = ("id", "nomDepart", "nbPers")

class SousReseauAdmin(admin.ModelAdmin):
    list_display = ("addressIP", "masque")

admin.site.register(Departement, DepartementAdmin)
admin.site.register(SousReseau, SousReseauAdmin)