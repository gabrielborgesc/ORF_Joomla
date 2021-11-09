#Imports
import glob
import re
import xml.etree.ElementTree as ET
from components import Component
import configparser

#Criação de arrays
permittedsArray = []
notpermittedsArray = []
standardComponents = []
namepermittedComponents = []
versionpermittedComponents = []

#Leitura dos componentes e versões permitidas
read_config = configparser.ConfigParser()
read_config.read("standardcomponents.ini")
namePermitted = read_config.get("Permitted", "name_version")
namesPermitted = namePermitted.split(",\n")
for x in namesPermitted:
    namepermittedComponents.append(x.split("_")[0])
    versionpermittedComponents.append(x.split("_")[1])



#Leitura dos componentes standard
read_config = configparser.ConfigParser()
read_config.read("standardcomponents.ini")
nameStandard = read_config.get("Standard", "name")
standardComponents = nameStandard.split(",\n")


#Script de separação de componentes
for file in glob.iglob('**/*.xml', recursive=True):
    tree = ET.parse(file)
    root = tree.getroot()
    for version in root.iter('version'):   
     filenames = file.split("/")
     componentName = filenames[1].split(".xml")[0]
     if ((componentName not in standardComponents) and componentName == filenames[0].split("_")[1]):

        component = Component(componentName, version.text)
        
        if (componentName in namepermittedComponents):
            permittedsArray.append(component)

        else:
            notpermittedsArray.append(component)
            
     



#Print de componentes permitidos ou não permitidos
for component in notpermittedsArray:
    print(component.name + " " + component.version)


    