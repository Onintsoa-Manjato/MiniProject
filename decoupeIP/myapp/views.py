from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Departement, SousReseau
from .forms import DepartementForm, sousReseauForm
from .graph import get_graph
from .caclulette import calc
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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

def log_out(request):
    logout(request)
    return redirect('login')

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

def departementlist(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    context["dataset"] = Departement.objects.all()

    return render(request, "departementlist.html", context)

def detail_departement(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    context["data"] = Departement.objects.get(id = id)

    return render(request, "detail_departement.html", context)

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

def delete_departement(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    obj = get_object_or_404(Departement, id = id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/departementlist/")
    
    return render(request, "delete_departement.html", context)

def sous_reseau(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    form2 = sousReseauForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        return HttpResponseRedirect("/calculateur/")
    context['form2'] = form2

    return render(request, "sousreseau.html", context)

def sousreseaulist(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    context["dataset2"] = SousReseau.objects.all()

    return render(request, "sousreseaulist.html", context)

def detail_sousreseau(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    context["data1"] = SousReseau.objects.get(id = id)

    return render(request, "detail_sousreseau.html", context)

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

def delete_sousreseau(request, id):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}

    obj2 = get_object_or_404(SousReseau, id = id)

    if request.method == "POST":
        obj2.delete()

        return HttpResponseRedirect("/sousreseaulist/")
    
    return render(request, "delete_sousreseau.html", context)

def calculateur(request):
    if not request.user.is_authenticated:
        return log_in(request)
    context = {}
    listRes = calc()
    
    context["dataset1"] = listRes

    return render(request, "calculateur.html", context)

def graph_view(request):
    if not request.user.is_authenticated:
        return log_in(request)
    # Get the graph
    graph = get_graph()

    # Render the graph to the template
    return render(request, 'graph.html', {'graph': graph})
