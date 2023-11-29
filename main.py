from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import photoresistor as PH
import DS18B20.py as TH
import soil_moisture as SM
import ADC0832
import RPi.GPIO as GPIO

# MQTT config (clientID must be unique within the AWS account)

# Init MQTT client


def init():
    ADC0832.setup()
    GPIO.setmode(GPIO.BCM)

def destroy():
    ADC0832.destroy()

# Send message to the iot topic
def send_data(message):
    mqttc.publish(topic, json.dumps(message), 0)
    print("Message Published")

# Loop until terminated
def loop():

    while(True):
        light = round(PH.main_iteration(), 2)
        temperature = TH.main_iteration()
        soil_moisture = SM.main_iteration()`

        print('Light: ' + light)
        print('Temperature: ' + temperature)
        print('Soil: ' + soil_moisture())
        time.sleep(1)

# Main
if __name__ == '__main__':
    print("Starting program...")
    init()
    try:
        # Connect

        # Main loop called
        loop()
    except KeyboardInterrupt:
        destroy()
        print ('The end !')