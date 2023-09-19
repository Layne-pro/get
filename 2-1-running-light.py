import RPi.GPIO as gpio
import time
leds=[2,3,4,17,27,22,10,9]
leds2=leds[::-1]
gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
for i in range(3):
    for i in range(8):
        gpio.output(leds[i], 1)
        time.sleep(0.2)
        gpio.output(leds[i],0)
    for i in range(0,8):
        gpio.output(leds2[i], 1)
        time.sleep(0.2)
        gpio.output(leds2[i],0)
gpio.output(leds, 0)
gpio.clenup()

