#Imports
import glob
import csv
import xml.etree.ElementTree as ET
from components import Component
import configparser
import os
import SQLSearch

def readComponents(path, sqlpath):

    #Criação de arrays
    permittedsArray = []
    notpermittedsArray = []
    standardComponents = []
    namepermittedComponents = []
    versionpermittedComponents = []
    Permitted_components =[]

    SQLSearch.execute(path, sqlpath)
    #Leitura dos componentes e versões permitidas
    read_config = configparser.ConfigParser()
    read_config.read("standardcomponents.ini")
    namePermitted = read_config.get("Permitted", "name_version")
    namesPermitted = namePermitted.split(",\n")
    for x in namesPermitted:
        n = x.split("_")[0]
        namepermittedComponents.append(x.split("_")[0])
        versionpermittedComponents.append(x.split("_")[1])
        v = x.split("_")[1]
        Permitted_components.append(Component(n, v)) #Array com Componentes permitidos e suas versoes (tabela)

    #Leitura dos componentes standard
    read_config = configparser.ConfigParser()
    read_config.read("standardcomponents.ini")
    nameStandard = read_config.get("Standard", "name")
    standardComponents = nameStandard.split(",\n")#Array


    #Script de separação de componentes do XML
    for file in glob.glob(os.path.join(path, '**','*.xml'), recursive=True):

        tree = ET.parse(file)
        root = tree.getroot()
        for version in root.iter('version'):
            filenames = file.split(os.sep)
            componentName = filenames[len(filenames)-1].split(".xml")[0]
            if ((componentName not in standardComponents) and componentName == filenames[len(filenames)-2].split("_")[1]):

                component = Component(componentName, version.text)

                if (componentName in namepermittedComponents):
                    permittedsArray.append(component)

                else:
                    notpermittedsArray.append(component)

    Components_used_permitted_version_ok = []
    Components_used_permitted_old_version = []
    Components_used_not_permitted = []

    s = SQLSearch.getAllComponents()

    for i in s:
     for j in Permitted_components:
         if i.name == j.name:
            if isNewerVersion(i.version,j.version):
              Components_used_permitted_version_ok.append(i)
            else:
              Components_used_permitted_old_version.append(i)

     if i.name not in standardComponents and i not in Components_used_permitted_version_ok and i not in Components_used_permitted_old_version:
       Components_used_not_permitted.append(i)

    print("********************Componentes Permitidos Atualizados***************************")
    for i in Components_used_permitted_version_ok:
        print(i.name + " " + i.version)
    CreateCSV("ComponentesPermitidosAtualizados.csv",Components_used_permitted_version_ok)

    print("******************Componentes Permitidos Desatualizados**************************")
    for i in Components_used_permitted_old_version:
       print(i.name + " " + i.version)
    CreateCSV("ComponentesPermitidosDesatualizados.csv", Components_used_permitted_old_version)

    print("***********************Componentes Não Permitidos*******************************")
    for i in Components_used_not_permitted:
        print(i.name + " " + i.version)
    CreateCSV("ComponentesNaoPermitidos.csv",Components_used_not_permitted)


def isNewerVersion(v1,v2): #Retorna true se v1 eh a versao mais recente ou a mesma que v2
    i = 0
    version1 = v1.split(".")
    version2 = v2.split(".")
    while True:
        if i >= len(version1) or i >= len(version2):
            if len(version2) > len(version1):
                return False
            else:
                return True
        if int(version1[i]) < int(version2[i]):
            return False
        elif int(version1[i]) > int(version2[i]):
            return True
        i += 1

def CreateCSV(filename,list):
    rows = []
    fields = ['Nome', 'Versao']
    for i in list:
        rows.append([i.name, i.version])
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


