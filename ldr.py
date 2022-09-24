import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
delayt= .1
value= 0 
ldr= 7
led = 11
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, False)
def rc_time(ldr):
    count = 0

    #first set pin number 7 as outpt
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delayt)

    #now let change pin 7 back to input
         GPIO.setup(ldr, GPIO.IN)

    #now we will do the counting until the pin goes high
        while(GPIO.input(ldr) == 0):
            count +=1
    
        return count

#catch when script is interrupted, cleanup correctly
try:
    while True:
        print("Ldr Value:")
        value = rc_time(ldr)
        print(value)
        if(value <= 10000):
            print("lights are ON")
            GPIO.output(led, True)
        if(value > 10000):
            print("lights are OFF")
            GPIO.output(led, False)
except Keyboardinterrupt:
    pass
finally:
    GPIO.cleanup()


