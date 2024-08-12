import requests

token = ...
url = "https://api.clashofclans.com/v1/players/%232GCJYLQUY"

headers = {"Authorization": "Bearer " + token}


response = requests.get(url, headers)
print(response.json)
