from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Departement, SousReseau
from .forms import DepartementForm, sousReseauForm
from .graph import get_graph
from .caclulette import calc
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#Création de nouveau utilisateur
def signup(request):
    context = {}
    if request.method == 'POST':
        form4 = UserCreationForm(request.POST)
        if form4.is_valid():
            user = form4.save()
            login(request, user)
            return redirect('login')
    else:
        form4 = UserCreationForm()
    context["form4"] = form4
    return render(request, 'signup.html', context)

#Connexion
def log_in(request):
    context = {}
    if request.method == "POST":
        form5 = AuthenticationForm(data=request.POST)
        if form5.is_valid():
            user = form5.get_user()
            login(request,user)
            return redirect('departementlist')
    else:
        form5 = AuthenticationForm()
    context["form5"] = form5
    return render(request,'login.html', context)

#Deconnection
def log_out(request):
    logout(request)
    return redirect('login')

#Ajout d'un nouveau departement
def departement(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    form = DepartementForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('departementlist')
    context['form'] = form
    return render(request, "departement.html", context)

#afficher liste des départements
def departementlist(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    context["dataset"] = Departement.objects.all()
    return render(request, "departementlist.html", context)

#afficher détail de département
def detail_departement(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    context["data"] = Departement.objects.get(id = id)
    return render(request, "detail_departement.html", context)

#Modifier nom ou nombre de personne dans département
def update_departement(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    obj = get_object_or_404(Departement, id = id)
    form1 = DepartementForm(request.POST or None, instance=obj)
    if form1.is_valid():
        form1.save()
        return HttpResponseRedirect("/departement/"+id)
    context["form1"] = form1
    return render(request, "update_departement.html", context)

#supprimer un département
def delete_departement(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    obj = get_object_or_404(Departement, id = id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/departementlist/")
    return render(request, "delete_departement.html", context)

#afficher le sous réseau
def sousreseaulist(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    context["dataset2"] = SousReseau.objects.all()
    return render(request, "sousreseaulist.html", context)

#modifier sous réseau
def update_sousreseau(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    obj1 = get_object_or_404(SousReseau, id = id)
    form3 = sousReseauForm(request.POST or None, instance=obj1)
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect("/sousreseaulist/")
    context["form3"] = form3
    return render(request, "update_sousreseau.html", context)

#Découpage sous réseau par département
def calculateur(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    listRes = calc()   
    context["dataset1"] = listRes
    return render(request, "calculateur.html", context)

#représentation graphique de nombre de machine max par département
def graph_view(request):
    if not request.user.is_authenticated:
        return log_in(request)
    graph = get_graph()
    return render(request, 'graph.html', {'graph': graph})
