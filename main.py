import urllib.request
import json

url = "http://py4e-data.dr-chuck.net/comments_2291781.json"

uh = urllib.request.urlopen(url)
data  = uh.read().decode()



data = json.loads(data)

times = 0

for i in data["comments"]:
    times += int(i["count"])

print(times)
