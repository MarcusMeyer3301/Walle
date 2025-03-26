# this file is for: #2 DETECT PAYLOAD
from machine import Pin, ADC
from time import sleep

# Reed swich on pin 0 using internal pull down resistor, other wire of switch connects to 3.3V
reed_switch = Pin(6, Pin.IN, Pin.PULL_DOWN)
led = Pin(3, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour
led2 = Pin(4, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour
led3 = Pin(5, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour

led.value(1)
led2.value(1)
led3.value(1)

ir = ADC(28) #GPIO 28 versus ADC2?
# You can also use the IR Photodiode as a digital input.
t_value = 2000 # threshold value that would indicate the presents of an IR emitter

while True:
    if reed_switch.value() == 1:  # Check if the magnet is near
        led3.value(0)# Turn on the LED
    
    else:
        led3.value(1)  # Turn off the LED

    if ir.read_u16() > t_value:
        led2.value(0) # turns LED on
    else:
        led2.value(1) # turns LED off
       
    
    print(reed_switch.value())
    sleep(0.1)  # Short delay