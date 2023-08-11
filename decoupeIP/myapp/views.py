from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .models import Departement, SousReseau
from .forms import DepartementForm, sousReseauForm
import ipaddress

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
    form = DepartementForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/departement/"+id)
    context["form"] = form
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

    form = sousReseauForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/calculateur/")
    context['form'] = form

    return render(request, "sousreseau.html", context)

def calculateur(request):
    reseau = list(SousReseau.objects.values_list('addressIP').first())[0]
    nbDepart = len(Departement.objects.all())
    context = {}
    listRes = []
    for i in range(nbDepart):
        res = {}
        nomDepart = list(list(Departement.objects.values_list('nomDepart'))[i])[0]
        nbPers = list(list(Departement.objects.values_list('nbPers'))[i])[0]
        if nbPers < 6 :
            prefixlenSR = '29'
        elif (nbPers >= 6) and (nbPers < 14):
            prefixlenSR = '28'
        elif (nbPers >= 14) and (nbPers < 30):
            prefixlenSR = '27'
        elif (nbPers >= 30) and (nbPers < 62):
            prefixlenSR = '26'
        elif (nbPers >= 62) and (nbPers < 126):
            prefixlenSR = '25'
        elif (nbPers >= 126) and (nbPers < 254):
            prefixlenSR = '24'
        elif (nbPers >= 254) and (nbPers < 510):
            prefixlenSR = '23'
        elif (nbPers >= 510) and (nbPers < 1022):
            prefixlenSR = '22'
        elif (nbPers >= 1022) and (nbPers < 2046):
            prefixlenSR = '21'
        elif (nbPers >= 2046) and (nbPers < 4094):
            prefixlenSR = '20'
        elif (nbPers >= 4094) and (nbPers < 8192):
            prefixlenSR = '19'     
        network = ipaddress.ip_network(reseau+'/'+prefixlenSR, strict=False)
        ip = ipaddress.ip_address(reseau)
        res["Nom Sous Réseau"] = nomDepart
        res["Nombre PC"] = nbPers
        res["Adresse réseau"] = reseau+'/'+prefixlenSR
        res["Masque sous réseau"] = network.netmask
        res["Passerelle"] = str(ip + 1)
        res["Broadcast"] = str(ip + network.num_addresses - 1)
        res["Inverse masque réseau"] = network.hostmask
        res["Nombre de Machine Max"] = network.num_addresses - 2
        listRes.append(res)
        reseau = str(ip + network.num_addresses)
    context["dataset"] = listRes

    return render(request, "calculateur.html", context)