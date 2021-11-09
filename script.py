import glob
import re
import xml.etree.ElementTree as ET
from components import Component

componentsArray = []
permittedsArray = []
notpermittedsArray = []
standardComponents = ["banners","contacts","joomlaupdate","messaging","multilingualassociations","newsfeeds"
, "postinstall", "redirect", "search", "smartsearch", "tags"]
permittedComponents = ["akeeba","securitycheck","phocadownload","phocagallery","jce","k2","youtubegallery"]


for file in glob.iglob('**/*.xml', recursive=True):
    tree = ET.parse(file)
    root = tree.getroot()
    for version in root.iter('version'):   
     filenames = file.split("/")
     componentName = filenames[1].split(".xml")[0]
     if (componentName not in standardComponents):
        component = Component(componentName, version.text)
        
        if (componentName in permittedComponents):
            permittedsArray.append(component)

        else:
            notpermittedsArray.append(component)
            
     




for component in permittedsArray:
    print(component.name + " " + component.version)


    
