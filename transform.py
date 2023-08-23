import xml.etree.ElementTree as ET

filein  = 'borrowed.xml'
fileout = 'transformed.xml'

# Register the namespaces in the original feed
namespaces = dict([node for _, node in ET.iterparse(filein, events=['start-ns'])])
for ns in namespaces:
    ET.register_namespace(ns, namespaces[ns])

# Parse the feed file
#tree = ET.parse(filein)
tree = ET.ElementTree(file=filein)
root = tree.getroot()

# Change the channel type from episodic to serial
#for type in root.iter('itunes:type'):
#typetag = root.find('itunes:type')
typetag = root.find("./channel/itunes:type", namespaces)
print ('DEBUG: ' + typetag.text)
typetag.text = "serial"
print ('DEBUG: ' + typetag.text)

tree  = ET.ElementTree(root)

# Output the new feed file
tree.write(fileout)
