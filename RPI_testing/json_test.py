import requests

x = requests.get('http://cpen291-27.ece.ubc.ca/data.json').json()
size = len(x['data'])
print(size)
print(x['data'][size - 1])