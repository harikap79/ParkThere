import requests
from bs4 import BeautifulSoup
import json


def getGeoCode(address):
	address += " Singapore"
	requesteddata = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}&key=AIzaSyCZFz2PlrkMfumZIKyCJlA7NS4MDRNFGhk'.format(address))
	soup = str(BeautifulSoup(requesteddata.content, 'html.parser'))
	soupdict = json.loads(soup)
	lat = soupdict['results'][0]['geometry']['location']['lat']
	lng = soupdict['results'][0]['geometry']['location']['lng']
	return lat, lng



