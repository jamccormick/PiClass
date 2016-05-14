#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

motorIn1 = 16
motorIn2 = 18
motorEnable = 22

GPIO.setup(motorIn1, GPIO.OUT)
GPIO.setup(motorIn2, GPIO.OUT)
GPIO.setup(motorEnable, GPIO.OUT)

print("Turning motor on.")

GPIO.output(motorIn1, GPIO.HIGH)
GPIO.output(motorIn2, GPIO.LOW)
GPIO.output(motorEnable, GPIO.HIGH)

sleep(2)

print("Stopping motor")

GPIO.output(motorIn1, GPIO.LOW)

GPIO.cleanup()


