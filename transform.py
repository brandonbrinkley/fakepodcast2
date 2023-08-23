import xml.etree.ElementTree as ET

namespaces = {'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd'}

tree = ET.parse('borrowed.xml')

for type in tree.getroot().iterfind('itunes:type', namespaces):
    type.text = "serial"

tree.write('transformed.xml')
