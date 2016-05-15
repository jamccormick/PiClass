import time
import argparse

#I have no idea what the device name is going to be
#So let's just pass it as a command line argument.
parser = argparse.ArgumentParser()
parser.add_argument("device")
args = parser.parse_args()
thermometer = args.device

#Provide a functuon to transform Celcius to Fahrenheit
def ctof(temp_c):
  return temp_c * 9.0 / 5.0 + 32.0 0

tfile = open(thermometer)

text = tfile.read()
tfile.close()
secondLine = text.split("\n")[1]
temperatureData = secondLine.split(" ")[9]

temperature = float(temperatureData[2:])

temperature = temperature / 1000
print(temperature)
