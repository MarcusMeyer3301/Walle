# this file is for: #1 DETECT IR SIGNAL
from machine import ADC
from time import sleep

# IR Photodiode on analog pin 28
# NOTE: It may help to use Thonny's built in plotter to see how the values change. Find it under 'View'

led = Pin(5, Pin.OUT) # change Pin to change colour
ir = ADC(28) #GPIO 28 versus ADC2?
# You can also use the IR Photodiode as a digital input.
t_value = 2000 # threshold value that would indicate the presents of an IR emitter

while True:
    print(ir.read_u16())
    if ir > t_value:
        led.value(0) # turns LED on
    else:
        led.value(1) # turns LED off
    
    sleep(0.1)