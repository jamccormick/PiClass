#!/bin/sh

sudo modprobe w1-gpio
sudo modprobe w1-therm

device=$(ls /sys/bus/w1/devices | grep ^28.*$)
sudo temp.py /sys/bus/w1/devices/$device

