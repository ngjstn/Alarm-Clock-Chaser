from multiprocessing import Process
import time 
from picamera import PiCamera
import board 
import requests
import datetime 
from digitalio import DigitalInOut, Direction, Pull
from motorControl import*
from clockBg import clockBg
from updateSong import updateSong
from getDict import getDict
from uploadImgur import uploadImg

# intialize camera object and define upload image path
camera = PiCamera()
camera.capture('/home/pi/Desktop/pi_camera/image.jpg')

# starts the clock display process in the background (check clockBg.py)
clock = Process(target = clockBg) 
clock.start() 

# define push button settings
button = DigitalInOut(board.D4) 
button.direction = Direction.INPUT
button.pull = Pull.DOWN

newDay = True;

# sends server request to get the dictionary data 
x = getDict()
hour = x['hour']
minute = x['minute']
print(hour)
print(minute)

# define time settings
local_timezone = datetime.timezone(datetime.timedelta(hours=+17))  
given_time = datetime.datetime.strptime(str(hour) + ':' + str(minute), "%H:%M").time()

# check if we have entered a new day 
if (given_time < datetime.datetime.now().astimezone(local_timezone).time()): 
    newDay = False 

# lookup which song was received in the server request (check updateSong.py)
song = updateSong(x['song'])

# main functionality loop
while True: 
    old_time = datetime.datetime.now().astimezone(local_timezone).time() 
    current_time = datetime.datetime.now().astimezone(local_timezone).time() 
    print(current_time)

    # check if the alarm time has been met or if we aren't in a new day, then stay in loop
    while given_time > current_time or not newDay: 
        time.sleep(0.01)
        old_time = current_time
        current_time = datetime.datetime.now().astimezone(local_timezone).time()
        print(current_time) 
        if old_time > current_time: 
            newDay = True 

        # send server request to check for any new alarms
        x2 = getDict()

        # check if the new alarm is today or tomorrow 
        if x2 != x:
            newDay = True
            hour = x2['hour']
            minute = x2['minute'] 
            x = x2 
            given_time = datetime.datetime.strptime(str(hour) + ':' + str(minute), "%H:%M").time()
            if (given_time < current_time): 
                newDay = False 
            song = updateSong(x2['song'])

    newDay = False
    print('exit while loop')
    song.play()
    
    # short delay to ensure song is actually playing
    while song.is_playing() == 0: 
        time.sleep(0.01)

    # waits for alarm button to be pressed
    while not button.value: 
        time.sleep(0.01)

        # intialize movement pathing algorithm
        pathingAlg()

        # if song finishes before button is pressed, loop back to beginning of the song
        if song.is_playing() == 0: 
            print("song ended... restarting")
            song.stop()
            song.play()
            while song.is_playing() == 0: 
                time.sleep(0.01)

    song.stop() 
    stop()

    # takes picture 
    print("button pushed")
    camera.capture('/home/pi/Desktop/image.jpg')

    # uploads image to Imgur, sends post request URL to server
    try:
        url = 'http://cpen291-27.ece.ubc.ca/api/img'
        myobj = {'url': uploadImg()} 
        x = requests.post(url, data= myobj) 
        
    except: 
        print("Error uploading image")





