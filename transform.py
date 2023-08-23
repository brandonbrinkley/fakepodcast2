import xml.etree.ElementTree as ET

namespaces = {
    'dc': 'http://purl.org/dc/elements/1.1/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'atom': 'http://www.w3.org/2005/Atom',
    'itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'anchor': 'https://anchor.fm/xmlns'
}

tree = ET.parse('borrowed.xml')

for type in tree.getroot().iterfind('ns1:type', namespaces):
    type.text = "serial"

tree.write('transformed.xml')
