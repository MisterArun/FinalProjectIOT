#!/usr/bin/env python

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
	print(temperature)
	return temperature

def main_iteration():
    temp = ds18b20Read()

def loop():
    while True:
        main_iteration()

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()
        print ('The end !')