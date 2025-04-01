# this file is for: #2 DETECT PAYLOAD
from machine import Pin
from time import sleep
from servo import Servo

# Reed swich on pin 0 using internal pull down resistor, other wire of switch connects to 3.3V
reed_switch = Pin(6, Pin.IN, Pin.PULL_DOWN)
led = Pin(3, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour
led2 = Pin(4, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour
led3 = Pin(5, Pin.OUT, Pin.PULL_DOWN) # change Pin to change colour

led.value(1)
led2.value(1)
led3.value(1)

#servos are on pin 8 and 9
servo_cam = Servo(Pin(9))
servo_hook = Servo(Pin(16))

# Motor A (left side of driver)
motor_a_in1 = Pin(13, Pin.OUT)
motor_a_in2 = Pin(14, Pin.OUT)
motor_a_en = PWM(Pin(15))
motor_a_en.freq(1000)
motor_a_correction = 1.03 # Adjust so both motors have same speed

# Motor B
motor_b_in3 = Pin(12, Pin.OUT)
motor_b_in4 = Pin(11, Pin.OUT)
motor_b_en = PWM(Pin(10)) # D6 on the driver
motor_b_en.freq(1000)

motor_b_correction = 1.1 # Adjust so both motors have same speed

# Function to control Motor A
def motor_a(direction = "stop", speed = 0):
    adjusted_speed = int(speed * motor_a_correction)  # Apply correction
    if direction == "forward":
        motor_a_in1.value(0)
        motor_a_in2.value(1)
    elif direction == "backward":
        motor_a_in1.value(1)
        motor_a_in2.value(0)
    else:  # Stop
        motor_a_in1.value(0)
        motor_a_in2.value(0)
    motor_a_en.duty_u16(int(adjusted_speed * 65535 / 100))  # Speed: 0-100%

# Function to control Motor B
def motor_b(direction = "stop", speed = 0):
    adjusted_speed = int(speed * motor_b_correction)  # Apply correction
    if direction == "forward":
        motor_b_in3.value(1)
        motor_b_in4.value(0)
    elif direction == "backward":
        motor_b_in3.value(0)
        motor_b_in4.value(1)
    else:  # Stop
        motor_b_in3.value(0)
        motor_b_in4.value(0)
    motor_b_en.duty_u16(int(adjusted_speed * 65535 / 100))  # Speed: 0-100%


claw_enabled = False

sleep(1)
servo_hook.move(130)
sleep(1)
servo_cam.move(82)

while True:
    if reed_switch.value() == 1:  # Check if the magnet is near
        led3.value(0)# Turn on the LED
        
        if not claw_enabled:
            servo_cam.move(5)
            sleep(1)
            servo_hook.move(70)
            sleep(1)
            
            
            
            i = 10
            while i < 82:
                servo_cam.move(i)
                i += 5
                sleep(0.05)
                
            claw_enabled = True
            
            #servo_cam.move(82)
    elif claw_enabled:
            led3.value(0)
            motor_a("forward", 25)
            motor_b("forward", 50)
            sleep(2)


            motor_a()
            motor_b()
            quit()
    else:
        led3.value(1)  # Turn off the LED
       
    
    print(reed_switch.value())
    sleep(0.1)  # Short delay
