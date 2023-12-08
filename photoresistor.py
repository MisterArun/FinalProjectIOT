#!/usr/bin/env python
import ADC0832
import time
import RPi.GPIO as GPIO


def init():
    pass

def destroy():
    pass

def main_iteration():
    res = ADC0832.getADC(1)
    vol = 5/255 * res
    lightStatus = ""
    #print ('analog value: %03d  ||  voltage: %.2fV' %(res, vol))
    
    # If the voltage is less than half its original value
    if (vol < 3.3/2):
        lightStatus = "Dark"
    else:
        lightStatus = "Light"
    
    #print(lightStatus)
    
    return [vol, lightStatus]


def loop():
    while True:
        main_iteration()
        
        time.sleep(0.2)

if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()
        print ('The end !')
