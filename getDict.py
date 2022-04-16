import requests

def getDict():
    x = requests.get('http://cpen291-27.ece.ubc.ca/api/data').json()
    y = requests.get('http://cpen291-27.ece.ubc.ca/api/data')
    
    while y.status_code != 200:
        print(y.status_code)
        x = requests.get('http://cpen291-27.ece.ubc.ca/api/data').json()
        y = requests.get('http://cpen291-27.ece.ubc.ca/api/data')
    #print(x)
    return x


#for local testing
# def getDict():
#     x = requests.get('http://localhost:9000').json()
#     y = requests.get('http://localhost:9000')
    
#     while y.status_code != 200:
#         print(y.status_code)
#         x = requests.get('http://localhost:9000').json()
#         y = requests.get('http://localhost:9000')
    
#     return x