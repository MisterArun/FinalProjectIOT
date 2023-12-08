from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import photoresistor as PH
import DS18B20 as TH
import soil_moisture as SM
import ADC0832
import RPi.GPIO as GPIO
import relay as pump

# MQTT config (clientID must be unique within the AWS account)
clientID = "736585036936"
endpoint = "a3r2erbmcexhjh-ats.iot.us-east-1.amazonaws.com" #Use the endpoint from the settings page in the IoT console
port = 8883
topic = "tb/aws/iot/projekt/IOT2 Project Device"

# Init MQTT client
mqttc = AWSIoTMQTTClient(clientID)
mqttc.configureEndpoint(endpoint,port)
mqttc.configureCredentials("certs/AmazonRootCA1.pem","certs/iot2project-private.pem.key","certs/iot2project-certificate.pem.crt")

# Actuators
LED = 25


def init():
    ADC0832.setup()
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(LED, GPIO.OUT)
    pump.init()

def destroy():
    ADC0832.destroy()

def lightOn():
    GPIO.setup(LED, GPIO.LOW)

def lightOff():
    GPIO.setup(LED, GPIO.HIGH)

# Send message to the iot topic
def send_data(message):
    mqttc.publish(topic, json.dumps(message), 0)
    print("Message Published")



# Loop until terminated
def loop():

    temp_thresh = 30
    soil_thresh = 200

    #temp_thresh = input("Enter the temperature threshold: ")
    #print('Temperature threshold is ' + str(temp_thresh))
    #soil_thresh = input("Enter the soil moisture threshold: ")
    #print('Soil moisture threshold is ' + str(soil_thresh))

    while(True):
        try:
            light = round(PH.main_iteration()[0], 2)
            temperature = TH.main_iteration()
            soil_moisture = SM.main_iteration()

            # Control light
            if(lightStatus == "Dark"):
                lightOn()
                print('Lamp on')
            else:
                lightOff()
            
            if(temperature > temp_thresh):
                print('Fan on')
            
            if(soil_moisture < soil_thresh):
                pump.motor_on()
                print('Motor running')
            else:
                motor_off()
            
            # Display
            print('Light: ' + lightStatus)
            print('Temperature: ' + str(temperature))
            print('Soil: ' + str(soil_moisture))
            print()

            # Formulate message
            message = {
                'temperature': temperature,
                'light': light,
                'soil_moisture': soil_moisture
            }

            # Send data to topic
            send_data(message)

        except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
        
        time.sleep(3)

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
