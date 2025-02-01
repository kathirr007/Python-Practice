import requests
# import json

response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code) # 200
persons_data = response.json()

for person in persons_data['people']:    
    print(person['name'])