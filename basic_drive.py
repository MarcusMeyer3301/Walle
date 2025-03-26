# in this file, we'll write functions to make the car drive in a st. line
# aswell as rotate, and reverse
from machine import Pin, PWM
from time import sleep

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


# Example

motor_a("forward", 25)
motor_b("forward", 50)
sleep(2)


motor_a()
motor_b()
