# this file is for: #2 DETECT PAYLOAD
from machine import Pin
from time import sleep

# Reed swich on pin 0 using internal pull down resistor, other wire of switch connects to 3.3V
reed_switch = Pin(6, Pin.IN, Pin.PULL_DOWN)
led = Pin(3, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour
led2 = Pin(4, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour
led3 = Pin(5, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour

led.value(1)
led2.value(1)
led3.value(1)

while True:
    if reed_switch.value() == 1:  # Check if the magnet is near
        led3.value(0)# Turn on the LED
    
    else:
        led3.value(1)  # Turn off the LED
       
    
    print(reed_switch.value())
    sleep(0.1)  # Short delay