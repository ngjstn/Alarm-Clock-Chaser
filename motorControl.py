import digitalio 
import board 
import time
import adafruit_hcsr04
import random

sonarRight = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D27)
sonarLeft = adafruit_hcsr04.HCSR04(trigger_pin=board.D21, echo_pin=board.D20)
sonarMiddle = adafruit_hcsr04.HCSR04(trigger_pin=board.D16, echo_pin=board.D26)

leftForward = digitalio.DigitalInOut(board.D5)
leftReverse = digitalio.DigitalInOut(board.D6)
rightForward = digitalio.DigitalInOut(board.D19)
rightReverse = digitalio.DigitalInOut(board.D13)

leftForward.direction = digitalio.Direction.OUTPUT
leftReverse.direction = digitalio.Direction.OUTPUT
rightForward.direction = digitalio.Direction.OUTPUT
rightReverse.direction = digitalio.Direction.OUTPUT

leftForward.value = False
leftReverse.value = False
rightForward.value = False
rightReverse.value = False

def forward():
    leftForward.value = True
    leftReverse.value = False
    rightForward.value = True
    rightReverse.value = False
    
def right():
    leftForward.value = True
    leftReverse.value = False
    rightForward.value = False
    rightReverse.value = True
    
def left():
    leftForward.value = False
    leftReverse.value = True
    rightForward.value = True
    rightReverse.value = False
    
def reverse():
    leftForward.value = False
    leftReverse.value = True
    rightForward.value = False
    rightReverse.value = True

def stop():
    leftForward.value = False
    leftReverse.value = False
    rightForward.value = False
    rightReverse.value = False

def leftTurn(): 
    leftForward.value = False
    leftReverse.value = True
    rightForward.value = True
    rightReverse.value = False
    time.sleep(0.4)

    rightForward.value = False 
    leftReverse.value = False 

def rightTurn(): 
    leftForward.value = True
    leftReverse.value = False
    rightForward.value = False
    rightReverse.value = True
    time.sleep(0.4)

    rightReverse.value = False 
    leftForward.value = False 

def sensorRead(sensor):
    dist = 100 
    try: 
        dist = sensor.distance 
    except RuntimeError: 
        pass 
    return dist 

def pathingAlg(): 
    #forward()
    leftDist = sensorRead(sonarLeft)
    rightDist = sensorRead(sonarRight) 
    middleDist = sensorRead(sonarMiddle)
    print("left: " + str(leftDist))
    print("right: " + str(rightDist))
    print("middle: " + str(middleDist))

    if rightDist < leftDist and rightDist < 15:
        while rightDist < 15: 
            print("1")
            rightDist = sensorRead(sonarRight)
            leftTurn()
    elif leftDist < rightDist and leftDist < 15: 
        while leftDist < 15:
            print("2")
            leftDist = sensorRead(sonarLeft)
            rightTurn()
    elif middleDist < 15: 
        if random.choice(("left", "right")) == "left": 
            
            print("3")
            leftTurn()
        else: 
            print("4")
            rightTurn()
    else: 
        forward()
    time.sleep(0.01)
   


# while True: 
#     forward()
#     time.sleep(2)
#     stop()