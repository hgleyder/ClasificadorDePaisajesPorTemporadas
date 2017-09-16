import weka.core.serialization as serialization
from weka.core.converters import Loader, Saver
import weka.core.jvm as jvm
from weka.core.classes import Random
from weka.classifiers import Classifier, Evaluation
from ImagePreprocesing import *

def getModelInstancesAttributes(filepath):
    with open(filepath) as f:
        contentInstances = f.readlines()

    Instances = []
    InstancesAtt = []

    for instance in contentInstances:
        Instances.append(instance.split(","))

    for ins in Instances:
        aux = []
        for att in ins:
            aux.append(int(att))
        InstancesAtt.append(aux)

    return InstancesAtt

def getModelInstancesClasses(filepath):
    Classes = []
    with open(filepath) as f:
        contentInstancesClasses = f.readlines()
    for instance in contentInstancesClasses:
        Classes.append(instance.replace("\n", ""))
    return Classes


def CrearInstanciaParaPredecir(path):
    colors = getMostRepresentativeColors(path)
    instancia = ""
    for color in colors:
        instancia += str(getGenericColorNameFromRGB(color[1])) + ","
    instancia += "?"
    return instancia

def PredecirUnaTemporada(path):
    jvm.start()
    insta = CrearInstanciaParaPredecir(path)
    atributos = ""
    file = open('ModelData/wekaHeader.arff', 'r')
    atributos = file.readlines()
    file.close()

    file = open('ModelData/predictionFiles/inst.arff', 'w')
    file.writelines(atributos)
    file.write("\n"+insta+'\n')
    file.close()

    objects = serialization.read_all("ModelData/77PercentModelPaisajes.model")
    classifier = Classifier(jobject=objects[0])

    loader = Loader()
    data = loader.load_file("ModelData/predictionFiles/inst.arff")
    data.class_is_last()


    clases = ["invierno", "verano", "otono", "primavera"]
    prediccion = ""
    for index, inst in enumerate(data):
        pred = classifier.classify_instance(inst)
        dist = classifier.distribution_for_instance(inst)
        prediccion = clases[int(pred)]
    jvm.stop()
    return prediccion