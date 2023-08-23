import xml.etree.ElementTree as ET

tree = ET.parse('borrowed.xml')

for type in tree.getroot().iterfind('itunes:type'):
    type.text = "serial"

tree.write('transformed.xml')
