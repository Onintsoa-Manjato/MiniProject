from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Departement, SousReseau
from .forms import DepartementForm, sousReseauForm
import ipaddress
from .graph import get_graph
from .caclulette import calc


def myapp(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def departement(request):
    context = {}

    form = DepartementForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form

    return render(request, "departement.html", context)

def departementlist(request):
    context = {}

    context["dataset"] = Departement.objects.all()

    return render(request, "departementlist.html", context)

def detail_departement(request, id):
    context = {}

    context["data"] = Departement.objects.get(id = id)

    return render(request, "detail_departement.html", context)

def update_departement(request, id):
    context = {}

    obj = get_object_or_404(Departement, id = id)
    form1 = DepartementForm(request.POST or None, instance=obj)
    if form1.is_valid():
        form1.save()
        return HttpResponseRedirect("/departement/"+id)
    context["form1"] = form1
    return render(request, "update_departement.html", context)

def delete_departement(request, id):
    context = {}

    obj = get_object_or_404(Departement, id = id)

    if request.method == "POST":
        obj.delete()

        return HttpResponseRedirect("/departementlist/")
    
    return render(request, "delete_departement.html", context)

def sous_reseau(request):
    context = {}

    form2 = sousReseauForm(request.POST or None)
    if form2.is_valid():
        form2.save()
        return HttpResponseRedirect("/calculateur/")
    context['form2'] = form2

    return render(request, "sousreseau.html", context)

def sousreseaulist(request):
    context = {}

    context["dataset2"] = SousReseau.objects.all()

    return render(request, "sousreseaulist.html", context)

def detail_sousreseau(request, id):
    context = {}

    context["data1"] = SousReseau.objects.get(id = id)

    return render(request, "detail_sousreseau.html", context)

def update_sousreseau(request, id):
    context = {}

    obj1 = get_object_or_404(SousReseau, id = id)
    form3 = sousReseauForm(request.POST or None, instance=obj1)
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect("/sousreseaulist/")
    context["form3"] = form3
    return render(request, "update_sousreseau.html", context)

def delete_sousreseau(request, id):
    context = {}

    obj2 = get_object_or_404(SousReseau, id = id)

    if request.method == "POST":
        obj2.delete()

        return HttpResponseRedirect("/sousreseaulist/")
    
    return render(request, "delete_sousreseau.html", context)

def calculateur(request):
    context = {}
    listRes = calc()
    
    context["dataset1"] = listRes

    return render(request, "calculateur.html", context)

def graph_view(request):
    # Get the graph
    graph = get_graph()

    # Render the graph to the template
    return render(request, 'graph.html', {'graph': graph})
