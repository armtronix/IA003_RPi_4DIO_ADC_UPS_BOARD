from time import sleep
import RPi.GPIO as GPIO
import os

#GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BOARD)

#PI GPIO INPUT PIN

pi_gpio_in_05 =29 #gpio 05

GPIO.setup(pi_gpio_in_05, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
      if GPIO.input(pi_gpio_in_05)==True:
               print("24v supply")
      else:
                 print("no supply")
    
