import requests
import json
from uk_covid19 import Cov19API


englandla = [
    #'areaCode!=Q',
    'areaCode>E00000000',
    'areaCode<E99999999',
    'date>=2020-07-01'
]

customStructure = {
    "date": "date",
    "areaType": "areaType",
    "areaName": "areaName",
    "areaCode": "areaCode",
        "cases 1": {
        "daily":"newCasesByPublishDate",
        "cumulative":"cumCasesByPublishDate"
    },
    "cases 2": {
    "newCasesBySpecimenDate": "newCasesBySpecimenDate",
    "cumCasesBySpecimenDate": "cumCasesBySpecimenDate"    
    },
    "deaths1": {
        "daily":"newDeathsByDeathDate",
        "cumulative":"cumDeathsByDeathDate"
    },
    "deaths2":{
        "newDeathsByPublishDate": "newDeathsByPublishDate",
        "cumDeathsByPublishDate": "cumDeathsByPublishDate"
    }
}

columns = {
    "areaType":"areaType"
,"areaName":"areaName"
,"date" : "date"
,"newCasesBySpecimenDate": "newCasesBySpecimenDate"
,"cumCasesBySpecimenDate": "cumCasesBySpecimenDate"    
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
        "daily":"newDeaths28DaysByPublishDate",
        "cumulative":"cumDeaths28DaysByPublishDate"
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
    "newDeaths28DaysByPublishDate": "newDeaths28DaysByPublishDate",
    "cumDeaths28DaysByPublishDate": "cumDeaths28DaysByPublishDate"
}

api = Cov19API(filters=englandla, structure=columns)  # Returns a dictionary
data = api.get_json("england.json")
print(data)
#ltlasDf = pd.DataFrame(data['data'])
#print(ltlasDf)


