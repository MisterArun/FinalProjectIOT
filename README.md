# FinalProjectIOT


## Modules
1. Sensors: DS18B20, ADC, Photoresistor, Soil Moisture, Relay, 2 LEDS, Water pump and a fan.

## How to install
- Clone the repository in your local machine using `git clone https://github.com/juliocesarfort/FinalProjectIOT`

## Setup sensors
Photoresistor: In channel 1 of the ADC.
Soil Moisture: In channel 0 of the ADC.
DS18B20: Pin 7.
2 LEDs: Pin 22 and 40.
Relay: Pin 36, Pump in COM(red), black one should go to GROUND.

## How to run the project
- Changed your certification in ther /certs folder.
- Change the cliendID, endpoint, port in main-publish.py 
- Run the main_publish to send data.
