import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
from .caclulette import calc

def get_graph():
    # Create a new figure and plot some data
    plt.figure()
    listRes = calc()
    x = []
    y = []
    for i in listRes:
        for key, val in i.items():
            if key == "Nom Sous Réseau":
                x.append(val)
            if key == "Nombre de Machine Max":
                y.append(val)
        plt.rcParams['axes.facecolor'] = '#777b80'
    fig = plt.figure()
    fig.patch.set_facecolor('#777b80')
    plt.title("Nombre de machine max par département")
    plt.xlabel("Departement")
    plt.ylabel("Nombre de machine max")
    plt.bar(x, y, color = "brown")

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')
