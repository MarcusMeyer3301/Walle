#psuedocode
'''
get readings from three ultrasonic sensors
Loop 
    check to see if any of the sensors read a distance less than 6 cm (or whatever distance). The best method for this, 
    would be a moving average. 
    with the moving average function, we will contiuously check whether the moving average is below the threshold
'''
from hcsr04 import HCSR04
from time import sleep
WINDOW_SIZE = 5 # maintain a window size 5 samples
arr1 = []
arr2 = []
arr3 = []
sensor1 = HCSR04(trigger_pin=22, echo_pin=19)
sensor2 = HCSR04(trigger_pin=21, echo_pin=18)
sensor3 = HCSR04(trigger_pin=20, echo_pin=17)
# for sensor 1
def push1(value):
    if len(arr1) < WINDOW_SIZE: 
        arr1.append(value)
    
    else:
        del arr1[0]
        arr1.append(value)
    #print(arr1)
def average1():
    return round(sum(arr1) / len(arr1), 2)
# for sensor 2
def push2(value):
    if len(arr2) < WINDOW_SIZE: 
        arr2.append(value)
    
    else:
        del arr2[0]
        arr2.append(value)
    #print(arr2)
def average2():
    return round(sum(arr2) / len(arr2), 2)
# for sensor 3
def push3(value):
    if len(arr3) < WINDOW_SIZE: 
        arr3.append(value)
    
    else:
        del arr3[0]
        arr3.append(value)
    #print(arr3)
def average3():
    return round(sum(arr3) / len(arr3), 2)
while True:
    dist1 = sensor1.distance_cm()
    dist2 = sensor2.distance_cm()    
    dist3 = sensor3.distance_cm()
    if dist1 > 0:
        push1(dist1)
    if dist2 > 0:
        push2(dist2)
    if dist3 > 0:
        push3(dist3)

    print(average1())
    print(average2())
    print(average3())
    print("\n\n")
    sleep(0.1)
