import RPi.GPIO as GPIO
import ADC0832
import time

def init():
    # Set the ADC
    ADC0832.setup()

    # Set the mode of the GPIO pins
    GPIO.setmode(GPIO.BCM)

def destroy():
    ADC0832.destroy()
    

def measure_soil_moisture_level():
    
    # ADC values
    res = ADC0832.getADC(0)
    vol = 3.3/255 * res
    
    # Calculate the soil moisture level in percentage
    soil_moisture_level = (vol * 100) / 1024
    
    # Print the soil moisture level
    #print('Soil moisture level: {}%'.format(soil_moisture_level))

    # Return the soil moisture level
    return soil_moisture_level

def main_iteration():
    return measure_soil_moisture_level()

def loop():
	while True:
		main_iteration()
		time.sleep(1)

if __name__ == '__main__':
    init()
    
    try:
        loop()
    except KeyboardInterrupt: 
        destroy()
        print ('The end !')
