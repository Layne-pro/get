import RPi.GPIO as gpio
leds=[2,3,4,17,27,22,10,9]
aux=[21,20,26,16,19,25,23,24]
gpio.setmode(gpio.BCM)
gpio.setup(leds,gpio.OUT)
gpio.setup(aux,gpio.IN)
gpio.output(leds,1)
while True:
    for i in range(8):
        gpio.output(leds[i], gpio.input(aux[i]))


