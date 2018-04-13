import requests
from bs4 import BeautifulSoup
import json


def getGeoCode(address):
    if ("/" in address[0:int(len(address)/2)]):
        address = deleteslashes(address)
    requesteddata = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyCZFz2PlrkMfumZIKyCJlA7NS4MDRNFGhk'.format(address))
    soup = str(BeautifulSoup(requesteddata.content, 'html.parser'))
    soupdict = json.loads(soup)
    try:
    	lat = soupdict['results'][0]['geometry']['location']['lat']
    	lng = soupdict['results'][0]['geometry']['location']['lng']
    except:
    	print(soupdict)
    	print(address)
    	return 0, 0
    return lat, lng

def deleteslashes(address):
        started = False
        for x in range(len(address)):
            if (started == True):
                if (address[x] == " "):
                    endofstring = address[x:]
                    break
            elif (address[x] == "/"):
                        startofstring = address[0:x]
                        started = True
        startofstring += endofstring
        return startofstring
        
