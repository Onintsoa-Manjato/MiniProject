from django.urls import path
from . import views
from .views import graph_view

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.log_in, name='login'), 
    path('logout/', views.log_out, name='logout'),
    path('departement/', views.departement, name='departement'),
    path('departementlist/', views.departementlist, name='departementlist'),
    path('departement/<id>', views.detail_departement, name="detail_departement"),
    path('departement/<id>/update/', views.update_departement, name="update_departement"),
    path('departement/<id>/delete/', views.delete_departement, name="delete_departement"),
    path('sousreseaulist/', views.sousreseaulist, name='sousreseaulist'),
    path('sousreseau/<id>/update/', views.update_sousreseau, name="update_sousreseau"),
    path('calculateur/', views.calculateur, name='calculateur'),
    path('graph/', graph_view, name='graph'),  
]