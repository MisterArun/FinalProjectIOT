import RPi.GPIO as GPIO
import time

def measure_soil_moisture_level(gpio_pin):

    # Set the mode of the GPIO pins
    GPIO.setmode(GPIO.BCM)
    
    # Set the gpio pin as an input pin
    GPIO.setup(gpio_pin, GPIO.IN)
    
    # Read the value from the gpio pin
    value = GPIO.input(gpio_pin)
    
    # Calculate the soil moisture level in percentage
    soil_moisture_level = (value * 100) / 1024
    
    # Return the soil moisture level
    return soil_moisture_level

if __name__ == '__main__':
    # Get the gpio pin number
    gpio_pin = int(input('Enter the gpio pin number: '))
    
    # Measure the soil moisture level
    soil_moisture_level = measure_soil_moisture_level(gpio_pin)
    
    # Print the soil moisture level
    print('Soil moisture level: {}%'.format(soil_moisture_level))