import requests

url = "https://cat-fact.herokuapp.com/facts"

response = requests.get(url)

if response.status_code == 200:
    json = response.json()
    count = 0
    while count < 5:
        dictionary = json[count]
        print(dictionary["text"])
        count += 1
else:
    print("Something wrong happened.")
