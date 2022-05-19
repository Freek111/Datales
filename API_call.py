from numpy import full
import requests
import pandas as pd
import json

URL = "https://opendata.cbs.nl/ODataFeed/OData/71488ned/"

URL2 = "https://opendata.cbs.nl/ODataFeed/OData/71488ned/TypedDataSet"

# Dit zijn de verschillende API's die aangeroepen kunnen worden.
API = ["TableInfos", "DataProperties", "CategoryGroups", "Geslacht", "Leeftijd", "RegioS", "Perioden"]

# Deze API's zijn te groot om op 1 pagina weer te geven waardoor er doorheen geloped moet worden.
API_long = ["UntypedDataSet", "TypedDataSet"]

api_json = "?$format=json"

params = {'$format': 'json'}




# Hieronder worden API's aangeroepen en opgeslagen als CSV bestanden en als JSON bestanden.

for api in API:
    url = URL + api + api_json

    r = requests.get(url)

    data = r.json()

    pd.DataFrame(data['value']).to_csv(f"CSV/{api}.csv", index=False)

    json_string = json.dumps(data)

    with open(f'JSON/{api}.json', 'w') as outfile:
        json.dump(json_string, outfile)






# Hieronder is een loop geschreven om meerdere pagina's van een API in een lijst samen te voegen en vervolgens op te slaan in een CSV bestand.

url = "https://opendata.cbs.nl/ODataFeed/OData/71488ned/TypedDataSet?$format=json"

Full_TypedDataSet = []

while True:

    r = requests.get(url)
    Full_TypedDataSet.extend(r.json()['value'])
    print(len(Full_TypedDataSet))
    
    if "odata.nextLink" in r.json():
        url = r.json()["odata.nextLink"]
        
    else:
        break

pd.DataFrame(Full_TypedDataSet).to_csv("CSV/TypedDataSet.csv", index=False)






















