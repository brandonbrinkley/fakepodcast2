import xml.etree.ElementTree as ET

filein  = 'borrowed.xml'
fileout = 'transformed.xml'

# Register the namespaces in the original feed
namespaces = dict([node for _, node in ET.iterparse(filein, events=['start-ns'])])
for ns in namespaces:
    ET.register_namespace(ns, namespaces[ns])

# Parse the feed file
tree = ET.ElementTree(file=filein)
root = tree.getroot()

# Remove generator tag
typetag = root.find("./channel/generator", namespaces)
typetag.remove()

# Change the channel type from episodic to serial
typetag = root.find("./channel/itunes:type", namespaces)
print ('Found type: ' + typetag.text)
typetag.text = "serial"
print ('Changed type : ' + typetag.text)

# Output the new feed file
tree  = ET.ElementTree(root)
tree.write(fileout)
