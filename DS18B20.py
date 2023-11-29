#!/usr/bin/env python
import time

def destroy():
    pass

def ds18b20Read():
	tfile = open("/sys/bus/w1/devices/28-020491771468/w1_slave")
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	temperature = round(temperature, 2)
	return temperature

def main_iteration():
    return ds18b20Read()

def loop():
	while True:
		print(main_iteration())
		time.sleep(1)

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()
        print ('The end !')
