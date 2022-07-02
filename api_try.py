import requests
import xml.etree.ElementTree as ET

r = requests.get('https://boardgamegeek.com/xmlapi2/thing?id=68264')

#print(r.content)

root = ET.fromstring(r.content)

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print(root[0][4])
print(root[0][4].text)