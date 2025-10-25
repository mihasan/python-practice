import urllib.request, urllib.parse
import json

location = input("Enter location: ")
address = location.strip()

url = "http://py4e-data.dr-chuck.net/opengeo?"


#create parameter list

param = dict()
param["q"] = address



final_url = url + urllib.parse.urlencode(param)+"&format=json"
print("final url", final_url)
uh = urllib.request.urlopen(final_url)
data  = uh.read().decode()
#print(data[:1000])
js = json.loads(data)
plus = js['features'][0]['properties']['plus_code']
print(plus)


