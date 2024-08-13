import webbrowser
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(url)

if response.status_code == 200:
    json = response.json()
    webbrowser.open(json["url"])
else:
    print("Something wrong happened.")
