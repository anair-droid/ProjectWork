import requests
import json
import pandas as pd
import io


# def getData():
#     baseurl = "https://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=e2c1bb4d2e4e8b86b54b474211f26b3f"
#     response = requests.get(baseurl,verify=False)
#     # print(response.json())
#     weatherData = response.json()
#     tabularData = weatherData['weather']
#     # print(tabularData)
#     # print(pd.DataFrame(tabularData, columns=["id", "main","description", "icon"]))
#     Data = pd.DataFrame(tabularData, columns=["id", "main", "description", "icon"])
#     return Data
#
# print(getData())

#
# data = {
# "username": "admin",
# "password": "Test@123",
# "mfaCode": 0
# }
# r = requests.post('http://srvban09rpavm01.corp.mphasis.com:8082/v1/authentication', data=json.dumps(data), verify=False)
# token = json.loads(r.text)['token']
#
# print(token)

def getData():

    data = {
    "username": "admin",
    "password": "Test@123",
    "mfaCode": 0
    }
    r = requests.post('http://srvban09rpavm01.corp.mphasis.com:8082/v1/authentication', data=json.dumps(data), verify=False)
    token = json.loads(r.text)['token']
    return token

print(getData())