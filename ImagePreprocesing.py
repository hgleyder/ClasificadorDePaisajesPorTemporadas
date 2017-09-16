from PIL import Image, ImageDraw
import webcolors

def DrawRepresentativesColors(colors, outfile, numcolors=20, swatchsize=20, resize=150):
    pal = Image.new('RGB', (swatchsize*numcolors, swatchsize))
    draw = ImageDraw.Draw(pal)
    posx = 0
    for count, col in colors:
        draw.rectangle([posx, 0, posx+swatchsize, swatchsize], fill=col)
        posx = posx + swatchsize

    del draw
    pal.save(outfile, "PNG")
    return colors


def getMostRepresentativeColors(infile, numcolors=20, swatchsize=20, resize=150):
    image = Image.open(infile)
    image = image.resize((resize, resize))
    result = image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)
    result.putalpha(0)
    colors = result.getcolors(resize*resize)
    return sorted(colors, reverse=True)


def getGenericColorNameFromRGB(rgb_triplet):
    min_colours = {}
    for key, name in webcolors.css21_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - rgb_triplet[0]) ** 2
        gd = (g_c - rgb_triplet[1]) ** 2
        bd = (b_c - rgb_triplet[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]



listOfColors = [ "aqua","black","fuchsia", "green", "grey","gray","blue", "lime", "maroon","navy", "olive","purple","red","silver","teal","white","yellow","orange"]