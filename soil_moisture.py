import RPi.GPIO as GPIO
import ADC0832
import time

def measure_soil_moisture_level():

    # Set the ADC
    ADC0832.setup()

    # Set the mode of the GPIO pins
    GPIO.setmode(GPIO.BCM)
    
    # ADC values
    res = ADC0832.getADC(0)
    vol = 3.3/255 * res
    
    
    # Calculate the soil moisture level in percentage
    soil_moisture_level = (vol * 100) / 1024
    
    # Return the soil moisture level
    return soil_moisture_level

if __name__ == '__main__':
    # Get the gpio pin number
    
    # Measure the soil moisture level
    soil_moisture_level = measure_soil_moisture_level()
    
    # Print the soil moisture level
    print('Soil moisture level: {}%'.format(soil_moisture_level))