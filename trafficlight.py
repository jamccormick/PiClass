#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

while True:
  GPIO.output(11, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(11, GPIO.LOW)
  time.sleep(2)
  GPIO.output(37, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(37, GPIO.LOW)
  time.sleep(2)
  GPIO.output(7, GPIO.HIGH)
  time.sleep(2)
  GPIO.output(7, GPIO.LOW)
  time.sleep(2)


