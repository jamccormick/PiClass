#!/usr/bin/env python3

import pygame
import RPi.GPIO as GPIO
import time

pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.init()

snd = pygame.mixer.Sound("/home/pi/Downloads/Music_Box.wav")

pins = [3, 5, 7, 11, 13, 15, 19, 21]
try:
    [GPIO.setup(i, GPIO.OUT) for i in pins]
    #your code goes here
finally:
    GPIO.cleanup()


def blink(pin):
    GPIO.output(pin,1)
    time.sleep(0.10)
    GPIO.output(pin, 0)
    time.sleep(0.10)
    return

def blinkforward():
    snd.play()
    for i in range(0,4):
        if i % 2 == 1:
            [blink(j) for j in pins]
        elif i % 2 == 0:
            [blink(j) for j in pins[::-1]]

