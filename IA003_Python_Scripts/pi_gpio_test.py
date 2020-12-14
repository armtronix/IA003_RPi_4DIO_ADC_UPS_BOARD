from time import sleep
import RPi.GPIO as GPIO
import os
#Edited by:Goutam G
#GPIO.setmode(GPIO.BOARD)

#PI GPIO OUTPUT PIN

pi_gpio_out_22 =15 #gpio 22
pi_gpio_out_17 =11 #gpio 17
pi_gpio_out_27 =13 #gpio 27
pi_gpio_out_04 =7 #gpio 07

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pi_gpio_out_22, GPIO.OUT)  
GPIO.setup(pi_gpio_out_17, GPIO.OUT)  
GPIO.setup(pi_gpio_out_27, GPIO.OUT)  
GPIO.setup(pi_gpio_out_04, GPIO.OUT) 

#PI GPIO INPUT PIN

pi_gpio_in_26 =37 #gpio 26
pi_gpio_in_13 =33 #gpio 13
pi_gpio_in_19 =35 #gpio 19
pi_gpio_in_06 =31 #gpio 06

GPIO.setup(pi_gpio_in_26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pi_gpio_in_13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pi_gpio_in_19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pi_gpio_in_06, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
      if GPIO.input(pi_gpio_in_26)==False:
         	 GPIO.output(pi_gpio_out_22, False)
                 print("gpio 22")
      
      if GPIO.input(pi_gpio_in_13)==False:
		 GPIO.output(pi_gpio_out_17, False)
		 print("gpio 13")

      if GPIO.input(pi_gpio_in_19)==False:
                 GPIO.output(pi_gpio_out_27, False)
		 print("gpio 27")

      if GPIO.input(pi_gpio_in_06)==False:
                 GPIO.output(pi_gpio_out_04, False)
		 print("gpio 04")
      else:
	         print("RASPBERRY GPIO TEST CODE")
		 GPIO.output(pi_gpio_out_22, True)
		 GPIO.output(pi_gpio_out_17, True)
		 GPIO.output(pi_gpio_out_27, True)
		 GPIO.output(pi_gpio_out_04, True)     
