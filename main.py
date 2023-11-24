from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
#import board
#import adafruit_dht
import thermistor as TH
import photoresistor as PH
import ADC0832
import RPi.GPIO as GPIO

# MQTT config (clientID must be unique within the AWS account)
clientID = "736585036936"
endpoint = "a3r2erbmcexhjh-ats.iot.us-east-1.amazonaws.com" #Use the endpoint from the settings page in the IoT console
port = 8883
topic = "raspberry/temphumid/nasplamq"

# Init MQTT client
mqttc = AWSIoTMQTTClient(clientID)
mqttc.configureEndpoint(endpoint,port)
mqttc.configureCredentials("certs/AmazonRootCA1.pem","certs/raspberry-private.pem.key","certs/raspberry-certificate.pem.crt")

def init():
    ADC0832.setup()
    GPIO.setmode(GPIO.BCM)

def destroy():
    ADC0832.destroy()
    GPIO.cleanup()

# Send message to the iot topic
def send_data(message):
    mqttc.publish(topic, json.dumps(message), 0)
    print("Message Published")

# Loop until terminated
def loop():

     while(True):
          try:

               light = round(PH.main_iteration(), 2)
               temperature = 2 #placeholder

          except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
               print(error.args[0])

# Main
if __name__ == '__main__':
    print("Starting program...")
    init()
    try:
        # Connect
        mqttc.connect()
        print("Connect OK!")

        # Main loop called
        loop()
    except KeyboardInterrupt:
        destroy()
        mqttc.disconnect()
        print ('The end !')
        exit()