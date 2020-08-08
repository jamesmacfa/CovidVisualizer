import requests
import json
from uk_covid19 import Cov19API

scotland = [
    'areaCode=S12000036'
]

cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate"
}

api = Cov19API(filters=scotland, structure=cases_and_deaths)  # Returns a dictionary
data = api.get_json()
print(data)
