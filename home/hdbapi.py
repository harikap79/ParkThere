import requests
from bs4 import BeautifulSoup
import json

def getHDBCarparks():
	requesteddata = requests.get('https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&limit=312')
	soup = str(BeautifulSoup(requesteddata.content, 'html.parser'))
	soupdict = json.loads(soup)
	hdbcarparks = soupdict['result']['records']
	return hdbcarparks
        	
    
