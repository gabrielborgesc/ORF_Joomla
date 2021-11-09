import xml.etree.ElementTree as ET
tree = ET.parse('items.xml')
root = tree.getroot()
x = ''
for version in root.iter('version'):
    print(version.text)
#     x = version.text

# print(x)
