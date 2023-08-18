from .models import SousReseau, Departement
import ipaddress

#fonction pour découper le réseau en sous réseau par département
def calc():
    #récupèration adress IP et nombre de département
    reseau = list(SousReseau.objects.values_list('addressIP').first())[0]
    nbDepart = len(Departement.objects.all())
    #Initialisation d'un liste pour stocker les résultats
    listRes = []
    for i in range(nbDepart):
        #Initialisation des résultats(Nom de sous réseau, nombre de PC, adresse réseau, masque de sous réseau,
        # passerelle, broadcast, inverse de masque de sous réseau et nombre de machine maximale)
        res = {}
        #récupèration nom de departement et nombre des personnes dans le département
        nomDepart = list(list(Departement.objects.values_list('nomDepart'))[i])[0]
        nbPers = list(list(Departement.objects.values_list('nbPers'))[i])[0]
        #condition pour avoir un masque sous réseau proportionnel aux nombre des personnes dans le département
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
        elif (nbPers >= 8192) and (nbPers < 16382):
            prefixlenSR = '18'
        elif (nbPers >= 16382) and (nbPers < 32766):
            prefixlenSR = '17'
        elif (nbPers >= 32766) and (nbPers < 65534):
            prefixlenSR = '16'   
        #On utilise le module ipaddress pour récuperer l'adresse réseau, le masque, l'inverse masque réseau
        # et les nombres des machines max dans le sous réseau        
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
    return listRes