import requests
import json
import urllib.parse


def search(query):
    request = requests.get("https://storeedgefd.dsx.mp.microsoft.com/v9.0/pages/searchResults?market=US&locale=en-US&deviceFamily=windows.desktop&query=" + urllib.parse.quote(query))
    response = request.text
    json_response = json.loads(response)
    results = []
    for i in json_response[1]["Payload"]["SearchResults"]:
        print(str(i["ProductId"]))
        print(str(i["Title"]))