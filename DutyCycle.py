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
pwm1 = GPIO.PWM(motorIn1, 100)
pwm2 = GPIO.PWM(motorIn2, 100)

pwm1.start(0)
pwm2.start(50)

GPIO.output(motorIn2, GPIO.LOW)
GPIO.output(motorEnable, GPIO.HIGH)

pauseTime = 0.02

try:
  while(True):
    for i in range(0, 50):
      pwm1.ChangeDutyCycle(i)
      pwm2.ChangeDutyCycle(50-i)
      sleep(pauseTime)
    for i in range(50, -1, -1):
      pwm1.ChangeDutyCyle(i)
      pwm2.changeDutyCycle(50-i)
      sleep(pauseTime)
except KeyboardInterrupt:
  print("Stopping motor")
  pwm1.stop()
  pwm2.stop()
  GPIO.cleanup()


