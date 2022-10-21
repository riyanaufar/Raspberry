import time
import board
import busio
import RPi.GPIO as GPIO
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


servo1PIN = 12
servo2PIN = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1PIN, GPIO.OUT)
GPIO.setup(servo2PIN, GPIO.OUT)

servoUp = GPIO.PWM(servo1PIN, 50) # GPIO 12 for PWM with 50Hz
servoDown = GPIO.PWM(servo2PIN, 50) # GPIO 13 for PWM with 50Hz

servoUp.start(2.5) # Initialization
servoDown.start(2.5) # Initialization

#Buat i2c bus
i2c = busio.I2C(board.SCL, board.SDA)

#buat ADC objek menggunakan i2c bus
ads = ADS.ADS1015(i2c)
ads.gain = 1

#create single-ended input on channel 0-3
chan1 = AnalogIn(ads, ADS.P0) #ldr left
chan2 = AnalogIn(ads, ADS.P1) #ldr right
chan3 = AnalogIn(ads, ADS.P2) #ldr up
chan4 = AnalogIn(ads, ADS.P3) #ldr down


#MAPPING LDR VALUE
def remap(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = int(value - leftMin) / int(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    # return int(rightMin + (valueScaled * rightSpan))
    return rightMin + (valueScaled * rightSpan)




#def mapping(x, in_min, in_max, out_min, out_max):
  # return int((x - in_min)*(out_max-out_min)/(in_max-in_min)+out_min)

#scaler_sensor = mapping(chan1.value, 0, 1023, 0, 300)

#def translate(value, leftMin, leftMax, rightMin, rightMax):
 #   leftSpan = leftMax - leftMin
  #  rightSpan = rightMax - rightMin

   # valueScaled = int(value - leftMin) / int(leftSpan)

    #return rightMin + (valueScaled * rightSpan)

while True:
    scaler_Sensor = remap(int(chan1.value), 0, 1023, 0, 300)
    print(scaler_Sensor)
    time.sleep(2)




#print("{:>5}\t{:>5}".format('raw', 'v'))

#while True:
 #   print("{:>5}\t{:>5.5f}".format(scaler_Sensor, chan1.voltage))
  #  time.sleep(0.1)
