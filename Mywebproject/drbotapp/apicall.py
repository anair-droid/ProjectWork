import requests
import json
baseurl = "https://api.upcitemdb.com/prod/trial/lookup"
parameters = {'upc': '0012993441012'}
response =  requests.get(baseurl,verify=False,params=parameters)
print(response.content)
content= response.content

info = json.loads(content)

#print(type(info))


#print(info)


jstr = json.dumps(info)
print(jstr)

with open("apioutput.json", "w") as outfile:
    outfile.write(jstr)