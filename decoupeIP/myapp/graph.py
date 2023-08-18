import matplotlib.pyplot as plt
import base64
from io import BytesIO
from .caclulette import calc

#fonction pour faire le graph par le module matplotlib
def get_graph():
    #création de figure
    plt.figure()
    #on met dans listRes les données qu'on va utiliser dans le graph
    #calc() est la fonction dans calculette.py qui fait le calcule de découpage d'address IP en sous réseau
    listRes = calc()
    #Initialisation x: nom de département et y: nombre de machine max
    x = []
    y = []
    #listRes est un liste et les éléments dans listRes sont des dictionnaires
    for i in listRes:
        for key, val in i.items():
            #on récupère seulement les valeurs des nom de sous réseau pour x
            if key == "Nom Sous Réseau":
                x.append(val)
            #on récupère seulement les valeurs de nombre de machine maximale pour y
            if key == "Nombre de Machine Max":
                y.append(val)
    #couleur de la background de la figure
    plt.rcParams['axes.facecolor'] = '#777b80'
    fig = plt.figure()
    fig.patch.set_facecolor('#777b80')
    #titre de la figure
    plt.title("Nombre de machine max par département")
    #titre de l'axe horizontale et verticale de la figure
    plt.xlabel("Departement")
    plt.ylabel("Nombre de machine max")
    #fonction bar() pour dessiner les bar graph de couleur brouwn
    plt.bar(x, y, color = "brown")

    #sauvegarde de la graph
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')
