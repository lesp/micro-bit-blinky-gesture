from microbit import *

def blinky():
    for i in range(10):
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        sleep(500)
        
while True:
    if accelerometer.was_gesture("shake"):
        blinky()