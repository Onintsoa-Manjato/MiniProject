import ipaddress
reseau = input()
nbDepart = int(input())
listRes = []
for _ in range(nbDepart):
    res = {}
    nomDepart = input()
    nbPers = int(input())
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

for i in listRes :
    for key, val in i.items():
        print(key,":", val) 
    print()
    print("--------------------------")
    print() 