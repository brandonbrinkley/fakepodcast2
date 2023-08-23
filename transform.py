import xml.etree.ElementTree as ET

filein  = 'borrowed.xml'
fileout = 'transformed.xml'

# Register the namespaces in the original feed
namespaces = dict([node for _, node in ET.iterparse(filein, events=['start-ns'])])
for ns in namespaces:
    ET.register_namespace(ns, namespaces[ns])

# Parse the feed file
tree = ET.parse(filein)

# Change the channel type from episodic to serial
for type in tree.getroot().iter('itunes:type'):
    type.text = "serial"

# Output the new feed file
tree.write(fileout)
