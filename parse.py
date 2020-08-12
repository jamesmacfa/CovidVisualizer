import requests
import json
from uk_covid19 import Cov19API




scotland = [
    'areaName=Aberdeen City',
    #'areaCode>=S00000000',
    #'areaCode<=S99999999',
    'date>=2020-08-11'
]

customStructure = {
    "date": "date",
    "areaType": "areaType",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "hash": "hash",
    "cases": {
        "daily":"newCasesByPublishDate",
        "cumulative":"cumCasesByPublishDate"
    },
    "deaths": {
        "daily":"newDeathsByDeathDate",
        "cumulative":"cumDeathsByDeathDate"
    },
    "specimenDate": {
    "newCasesBySpecimenDate": "newCasesBySpecimenDate",
    "cumCasesBySpecimenDate": "cumCasesBySpecimenDate"    
    }
}

structureAll ={
    "date": "date",
    "areaType": "areaType",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "hash": "hash",
    "cases": {
        "daily":"newCasesByPublishDate",
        "cumulative":"cumCasesByPublishDate"
    },
    "deaths": {
        "daily":"newDeathsByDeathDate",
        "cumulative":"cumDeathsByDeathDate"
    },
    "specimenDate": {
    "newCasesBySpecimenDate": "newCasesBySpecimenDate",
    "cumCasesBySpecimenDate": "cumCasesBySpecimenDate"    
    },
    "maleCases": "maleCases",
    "femaleCases": "femaleCases",
    "newPillarOneTestsByPublishDate": "newPillarOneTestsByPublishDate",
    "cumPillarOneTestsByPublishDate": "cumPillarOneTestsByPublishDate",
    "newPillarTwoTestsByPublishDate": "newPillarTwoTestsByPublishDate",
    "cumPillarTwoTestsByPublishDate": "cumPillarTwoTestsByPublishDate",
    "newPillarThreeTestsByPublishDate": "newPillarThreeTestsByPublishDate",
    "cumPillarThreeTestsByPublishDate": "cumPillarThreeTestsByPublishDate",
    "newPillarFourTestsByPublishDate": "newPillarFourTestsByPublishDate",
    "cumPillarFourTestsByPublishDate": "cumPillarFourTestsByPublishDate",
    "newAdmissions": "newAdmissions",
    "cumAdmissions": "cumAdmissions",
    "cumAdmissionsByAge": "cumAdmissionsByAge",
    "cumTestsByPublishDate": "cumTestsByPublishDate",
    "newTestsByPublishDate": "newTestsByPublishDate",
    "covidOccupiedMVBeds": "covidOccupiedMVBeds",
    "hospitalCases": "hospitalCases",
    "plannedCapacityByPublishDate": "plannedCapacityByPublishDate",
    "newDeathsByPublishDate": "newDeathsByPublishDate",
    "cumDeathsByPublishDate": "cumDeathsByPublishDate",
    "newDeathsByDeathDate": "newDeathsByDeathDate",
    "cumDeathsByDeathDate": "cumDeathsByDeathDate",
    "femaleDeaths": "femaleDeaths",
    "maleDeaths": "maleDeaths"
}

api = Cov19API(filters=scotland, structure=customStructure)  # Returns a dictionary
data = api.get_json("scotland.json")
print(data)

