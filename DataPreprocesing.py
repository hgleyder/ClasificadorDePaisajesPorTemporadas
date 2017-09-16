import os
from ImagePreprocesing import *

def NuevoModelo():
    with open("instances.txt", "w") as myfile:
        myfile.close()

    with open("classes.txt", "w") as myfile:
        myfile.close()


NuevoModelo()
temporadas = ["invierno", "otono", "verano", "primavera"]
for temporada in temporadas:
    for file in os.listdir('modelImages/'+temporada):
        colors = getMostRepresentativeColors('modelImages/'+temporada+'/'+file)
        instancia = ""
        classification = temporada
        for color in colors:
             #instancia+=str(listOfColors.index(getGenericColorNameFromRGB(color[1])))+","
            instancia+=str(getGenericColorNameFromRGB(color[1]))+","
        #instancia=instancia[:-1]
        instancia += classification
        with open("instances.txt", "a") as myfile:
            myfile.write(instancia+"\n")
        with open("classes.txt", "a") as myfile:
            myfile.write(classification + "\n")
