# this file is for: #2 DETECT PAYLOAD
from machine import Pin
from time import sleep

# Reed swich on pin 0 using internal pull down resistor, other wire of switch connects to 3.3V
reed_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin('LED', Pin.OUT)

while True:
    if reed_switch.value() == 1:  # Check if the magnet is near
        led.value(1)# Turn on the LED
        sleep(0.5)
        led.value(0)# Turn off to blink
        sleep (0.2)
        
    else:
        led.value(0)  # Turn off the LED
       
    
    print(reed_switch.value())
    sleep(0.1)  # Short delay