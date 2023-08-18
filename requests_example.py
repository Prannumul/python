import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()
#print(json)
print("Number of people in space " + str(json["number"]))
i=1
for people in json["people"]:
    print(str(i) + ": " + people["name"])
    i=i+1