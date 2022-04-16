import requests

x = requests.get('https://w3schools.com/python/demopage.htm')
print(type(x))
print(x.text) 