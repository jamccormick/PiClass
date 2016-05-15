import time
import RPi.GPIO as io
io.setmode(io.BOARD)
io.setwarnings(False)

irPin = 18
powerPin = 16

io.setup(irPin, io.IN)
io.setup(powerPin, io.OUT)
io.output(powerPin, False)

while True:
  out = io.input(irPin)
  if out == 0:
    print("POWER ON")
    io.output(powerPin, True)
    time.sleep(1)
    print("POWER OFF")
    io.output(powerPin, False)
    time.sleep(1)
  time.sleep(0.5)


