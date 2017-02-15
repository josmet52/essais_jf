import RPi.GPIO as GPIO
import time

# Constantes
GPIO_output = 12
LED_status=False
LED_off = False
LED_frequence = 5 # frequence de clignotement de la LED en Hertz
LED_period = 1.0 / LED_frequence / 2 # temps de pause entre chaque changement d'état de la LED

## Init GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_output,GPIO.OUT)
GPIO.output(GPIO_output,LED_off)

try:
    print("runing, CTRL-C to stop")
    # boucle sans fin -> CTRL-C pour terminer
    while True:
        LED_status = not LED_status
        GPIO.output(GPIO_output,LED_status)
        time.sleep(LED_period)
        
except KeyboardInterrupt:
    print("bye")
    GPIO.output(GPIO_output,LED_off)
    pass
