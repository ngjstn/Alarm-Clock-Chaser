import time
import board
import adafruit_hcsr04

sonarRight = adafruit_hcsr04.HCSR04(trigger_pin=board.D17, echo_pin=board.D27)
sonarLeft = adafruit_hcsr04.HCSR04(trigger_pin=board.D21, echo_pin=board.D20)
sonarMiddle = adafruit_hcsr04.HCSR04(trigger_pin=board.D16, echo_pin=board.D26)

def sensorRead(sensor):
    dist = 100 
    try: 
        dist = sensor.distance 
    except RuntimeError: 
        pass 
    return dist 


while True:
    
    print("Right: " + str(sensorRead(sonarRight)))
    #print("Left: " + str(sensorRead(sonarLeft)))
    #print("Middle: " + str(sensorRead(sonarMiddle)))

    time.sleep(0.1)