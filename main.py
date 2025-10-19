# import urllib.request, urllib.error, urllib.parse
# from bs4 import BeautifulSoup

# url = input("enter the url: ")
# count = int(input("enter the count: "))
# position = int(input("enter the position: "))

# for i in range(count):
#     html = urllib.request.urlopen(url).read()
#     soup = BeautifulSoup(html, "html.parser")
    
#     tag = soup("a")
#     url = tag[position -1].get("href", None)
#     print("Retriving", url)
#     name = url.split("_")[-1].split(".")[0]
# print(name)


import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2291780.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
count = 0
for result in counts:
    # Debug print the data :)
    print(result.text)
    nums.append(result.text)
    count = int(result.text)+count

print('Count:', len(nums))
print('Sum:', count)