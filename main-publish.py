from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import photoresistor as PH
import DS18B20 as TH
import soil_moisture as SM
import ADC0832
import RPi.GPIO as GPIO

# MQTT config (clientID must be unique within the AWS account)
clientID = "736585036936"
endpoint = "a3r2erbmcexhjh-ats.iot.us-east-1.amazonaws.com" #Use the endpoint from the settings page in the IoT console
port = 8883
topic = "tb/aws/iot/projekt/IOT2 Project Device"


# Init MQTT client
mqttc = AWSIoTMQTTClient(clientID)
mqttc.configureEndpoint(endpoint,port)
mqttc.configureCredentials("certs/AmazonRootCA1.pem","certs/iot2project-private.pem.key","certs/iot2project-certificate.pem.crt")

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
        try:
            light = round(PH.main_iteration(), 2)
            temperature = 2 #TH.main_iteration()
            soil_moisture = SM.main_iteration()

            print('Light: ' + str(light))
            print('Temperature: ' + str(temperature))
            print('Soil: ' + str(soil_moisture))
            print()

            message = {
                'temperature': temperature,
                'light': light,
                'soil_moisture': soil_moisture
            }

            # Send data to topic
            send_data(message)

            time.sleep(3)
        except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])

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
