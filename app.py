import RPi.GPIO as GPIO
import time

# The following Python code can be used to will blink an LED connected to GPIO pin 18.

GPIO.setmode(GPIO.BCM)
led_pin = 17
GPIO.setup(led_pin, GPIO.OUT)

while(True):
   GPIO.output(led_pin, GPIO.HIGH)
   time.sleep(1)
   GPIO.output(led_pin, GPIO.LOW)
   time.sleep(1)
