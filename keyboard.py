import curses
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
stdscr = curses.initscr()
curses.cbreak()
print("Press 'q' to exit.")
print("Press 'a' to turn the LED on.")
quit = False
while not quit:
    c = stdscr.getch()
    if curses.keyname(c)=="a":
        GPIO.output(7, 1)
        time.sleep(0.01)
        GPIO.output(7, 0)
    elif curses.keyname(c)=="q":
        quit = True


