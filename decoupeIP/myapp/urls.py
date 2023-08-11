from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.myapp, name='myapp'),
    path('departement/', views.departement, name='departement'),
    path('departementlist/', views.departementlist, name='departementlist'),
    path('departement/<id>', views.detail_departement, name="detail_departement"),
    path('departement/<id>/update/', views.update_departement, name="update_departement"),
    path('departement/<id>/delete/', views.delete_departement, name="delete_departement"),
    path('sousreseau/', views.sous_reseau, name='sousreseau'),
    path('calculateur/', views.calculateur, name='calculateur'),
]