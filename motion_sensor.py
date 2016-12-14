#!/usr/bin/env python
"""
	Detects motion and outputs a sound via a piezo buzzer. 
"""

import RPi.GPIO as GPIO
import time

__author__ = "gus-pimylifeup"
__version__ = "1.0"
__maintainer__ = "pimylifeup.com"

pir_sensor = 11
piezo = 7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(piezo,GPIO.OUT)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            GPIO.output(piezo,True)
            time.sleep(1)
            GPIO.output(piezo,False)
            time.sleep(5)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
