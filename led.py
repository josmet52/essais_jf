"""
This small program causes a led to flash at a given frequency
    GPIO channel = 12
    Frequency = 5 Hz
"""

import RPi.GPIO as GPIO 
import time

# Constants
GPIO_channel_number = 12 # channel used --> setmode = GPIO.BCM
LED_off = False
LED_status = LED_off

# LED blink frequency in Hertz (number of flashs every second)
LED_blink_frequency = 5
# pause time between each change in the state of the LED
LED_half_period = 1.0 / LED_blink_frequency / 2 

# Init GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# set GPIO_channel_number in output mode
GPIO.setup(GPIO_channel_number,GPIO.OUT)
GPIO.output(GPIO_channel_number,LED_status) # init the LED to OFF

try:
    print("runing, CTRL-C to stop")
    print("blink frequency = " + str(LED_blink_frequency))
    # endless loop -> CTRL-C to stop
    while True:
        # change the status of the LED (1 -> 0 si 0 -> 1)
        LED_status = not LED_status
        # apply state to output
        GPIO.output(GPIO_channel_number,LED_status)
        # apply the pause time to respect the frequency
        time.sleep(LED_half_period)
        
except KeyboardInterrupt:
    print("bye")
    GPIO.output(GPIO_channel_number,LED_off) # switch the LED OFF
    pass
