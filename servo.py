#!/usr/bin/python3
#Paramveer Singh
from signal import signal, SIGTERM, SIGHUP, pause
from gpiozero import Servo, Button, PWMLED
from time import sleep


def safe_exit(signum, frame):
    exit(1)

def move_left():
    if left.held_time > (right.held_time or 0):
        if servo.value > -1:
         servo.value -= 0.01
         led.value = (servo.value+1)/2   

def move_right():
    if right.held_time > (left.held_time or 0):
        if servo.value < 1: servo.value += 0.01
    if servo.value >= 1: led.blink(0.2)
    else: led.value = (servo.value+1)/2
            
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

servo = Servo(18, min_pulse_width = 0.4/1000, max_pulse_width = 2.5/1000)
left = Button(16, hold_time = 0.01, hold_repeat = True)
right = Button(20, hold_time = 0.01, hold_repeat = True)
led = PWMLED(13)
try:
    left.when_held = move_left
    led.value = 1
    right.when_held = move_right
    
    pause()

except KeyboardInterrupt:
    pass

finally:
    servo.mid()
    sleep(0.5)
