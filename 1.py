import RPi.GPIO as gpio
import time
leds=[2,3,4,17,27,22,10,9]
gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
while True:
    for i in range(8):
        if input():
            break
        gpio.output(leds[i], 1)
        time.sleep(0.2)
        gpio.output(leds[i],0)
    
gpio.output(leds, 0)
gpio.clenup()

