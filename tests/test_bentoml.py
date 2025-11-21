import requests

url = "http://localhost:3000/predict"

data = {
    "input_data": {
        "ThirdLargestPropertyUseType": "Other",
        "PropertyGFABuilding(s)": 1234,
        "SecondLargestPropertyUseType": "Office",
        "DataYear": 2020,
        "PropertyGFATotal": 48210,
        "YearsENERGYSTARCertified": 10,
        "ListOfAllPropertyUseTypes": "Office,Other",
        "PrimaryPropertyType": "Office",
        "Latitude": 48.85,
        "BuildingType": "Multifamily",
        "PropertyGFAParking": 500,
        "Longitude": 2.35,
        "ThirdLargestPropertyUseTypeGFA": 0,
        "City": "Paris",
        "NumberofFloors": 5,
        "LargestPropertyUseTypeGFA": 30000,
        "LargestPropertyUseType": "Office",
        "PropertyGFATotal_log1p": 10.78,
        "YearBuilt": 1990,
        "SecondLargestPropertyUseTypeGFA": 10000,
        "AgeBuilding": 33,
        "NumberofBuildings": 2,
        "State": "NY"
    }
}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response JSON:", response.json())
