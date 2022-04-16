import requests
import time
import datetime
from uploadImgur import uploadImg

local_timezone = datetime.timezone(datetime.timedelta(hours=+17))  
try:
    url = 'http://cpen291-27.ece.ubc.ca/api/img'
    myobj = {'url': uploadImg(), 'time' : str(datetime.datetime.now().astimezone(local_timezone).time())}  
    #x = requests.post(url, data= myobj) 
    
    while True: 
        x = requests.post(url, data= myobj) 
        print("request sent")
        print(myobj)
        time.sleep(1)
except: 
    print("Error uploading image")

