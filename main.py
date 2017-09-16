from ImagePreprocesing import *

colors = getMostRepresentativeColors("Images/nat.jpg")

for color in colors:
    print getGenericColorNameFromRGB(color[1])