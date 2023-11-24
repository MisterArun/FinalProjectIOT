#!/usr/bin/env python
import ADC0832
import time
import math

def init():
  pass

def destroy():
  pass

def main_iteration():
  res = ADC0832.getADC(0)
  Vr = 3.3 * float(res) / 255
  Rt = (3.3 * 10000 / Vr) - 10000
  temp = 1/(((math.log(Rt / 10000)) / 3455) + (1 / (273.15+25)))
  Cel = temp - 273.15
  Fah = Cel * 1.8 + 32
  print ('Rt : %.2f | Celsius: %.2f C | Fahrenheit: %.2f F' %(Rt, Cel, Fah))

  return Cel

def loop():
  while True:
    main_iteration()

    time.sleep(0.2)
   
if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt: 
        ADC0832.destroy()
        print ('The end !')