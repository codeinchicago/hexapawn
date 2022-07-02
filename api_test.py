"""
Pokemon API Wrapper
Create a python wrapper for the Pokemon API. It should take in a pokemon name and display the pokemon with its height and weight
"""

import requests
import xml.etree.ElementTree as ET

def pokefinder():

    #lookup = requests.get(f"https://boardgamegeek.com/xmlapi2/search?query=dogs")
    r = requests.get(f"https://boardgamegeek.com/xmlapi2/thing?id=68264")

    if r.status_code == 200:
        print("Board game found, here is the information.")

    print(r.content)

    root = ET.fromstring(r.content)

    for child in root.iter('*'):
        print(child.tag)

    xmlDict = {}
    for sitemap in root:
        children = list(sitemap)
        xmlDict[children[0].text] = children[1].text
    print(xmlDict)

    print(r['name'])








pokefinder()

#Searching for items, dogs in this case.
#exact=1 to limit results to items that match the query exaclty.
#type=TYPE, limit to boardgames, TYPE=boardgame

#Example search for dogs.
#https://boardgamegeek.com/xmlapi2/search?query=dogs

#Searching for a game:
# https://boardgamegeek.com/xmlapi2/thing?id=68264