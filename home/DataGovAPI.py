from bs4 import BeautifulSoup
import requests
import json

def getCarParks():
    carparks = requests.get('https://data.gov.sg/api/action/datastore_search?resource_id=e2468b11-6cac-42e4-8891-145c4fc1cba2&limit=360')
    soup = BeautifulSoup(carparks.content, 'html.parser')
    soupstring = str(soup)
    soupdict = json.loads(soupstring)
    soupresults = soupdict['result']
    souprecords = soupresults['records']
    return souprecords
