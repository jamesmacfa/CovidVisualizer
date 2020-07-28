import requests
import json

response = requests.get('https://api.covid19uk.live')
result = response.json()

print (result)


