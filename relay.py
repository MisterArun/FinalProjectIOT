#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RelayPin = 16    # pin16

# GPIO setup
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RelayPin, GPIO.OUT)

def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH) # Turn motor on

def motor_off(pin):
    GPIO.output(pin, GPIO.LOW) # Turn motor off


if __name__ == '__main__':
    try:
        init()
        motor_on(RelayPin)
        print("motor on")
        time.sleep(1)
        motor_off(RelayPin)
        print("motor off")
        time.sleep(1)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        pass