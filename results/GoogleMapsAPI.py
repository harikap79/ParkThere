from bs4 import BeautifulSoup
import requests
import json
from urllib.request import urlopen
        
def calcDistance(origin, destination):
        addeddestination = destination
        addeddestination +=  " Singapore"
        distance = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={}&destinations={}&key=AIzaSyCZFz2PlrkMfumZIKyCJlA7NS4MDRNFGhk'.format(origin, addeddestination))
        soup = BeautifulSoup(distance.content, 'html.parser')
        soupstring = str(soup)
        soupdict = json.loads(soupstring)
        try:
            distanceinkm = soupdict['rows'][0]['elements'][0]['distance']['text']
        except (KeyError, IndexError):
            return 5
        if (distanceinkm[-2:] == " m"):
            distanceinkm = float(distanceinkm[0:len(distanceinkm)-2])
            distanceinkm = distanceinkm * 0.001
        else:
            distanceinkm = float(distanceinkm[0:len(distanceinkm)-3])
        return distanceinkm

