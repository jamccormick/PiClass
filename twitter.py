import time
import subprocess
import RPi.GPIO as GPIO
from twython import Twython
import picamera

SYSTEM_READY = 10
SYSTEM_RUNNING = 16
BUTTON = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SYSTEM_READY, GPIO.OUT)
GPIO.setup(SYSTEM_RUNNING, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

imgWidth="1280"
imgHeight="720"
imgName="tweetPic.jpg"

apiKey = ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''

snapCommand = "raspistill -w" + imgWidth + " -h" + imgHeight + " -o" + imgName

api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)

#set ready LED (red) on
GPIO.output(SYSTEM_READY, True)
#set working LED (green) off
GPIO.output(SYSTEM_RUNNING, False)
#print a statement saying that the system is ready

cam = picamera.PiCamera()

try: 
  while True:
    GPIO.wait_for_edge(BUTTON, GPIO.RISING)
    print("Program Running...\n")
    GPIO.output(SYSTEM_READY, False)
    GPIO.output(SYSTEM_RUNNING, True)
    
    print("Capturing photo...\n")
    cam.capture(imgName)
    photo = open(imgName, 'rb')
    
    print("Uploading photo to Twitter...\n")
    mediaStatus = api.upload_media(media=photo)
    
    timeNow = time.strftime("%H:%M:%S")
    dateNow = time.strftime("%d/%m/%Y")
    tweetText = "Photo captured by %twybot at " + timeNow + " on" + dateNow
    api.update_status(media_ids=[mediaStatus['media_id']], status = tweetText)

    #Turn off the running LED
    GPIO.output(SYSTEM_READY, True)
    #Turn on the ready LED
    GPIO.output(SYSTEM_RUNNING, False)
except KeyboardInterrupt:
  pass
finally:
  GPIO.cleanup()

