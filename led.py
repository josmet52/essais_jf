import RPi.GPIO as GPIO 
import time

# Constantes
GPIO_channel_number = 12 # channel used --> setmode = GPIO.BCM
LED_status=False
LED_off = False

# frequence de clignotement de la LED en Hertz (nombre de flashs par seconde)
LED_frequence = 2
# temps de pause entre chaque changement d'état de la LED
# utiliser 1.0 (et pas 1) pour que la variable LED_period soit un float
LED_half_period = 1.0 / LED_frequence / 2 

# Init GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# mettre la sortie GPIO_output en mode sortie
GPIO.setup(GPIO_channel_number,GPIO.OUT)
# initialiser la LED a OFF
GPIO.output(GPIO_channel_number,LED_off)

try:
    print("runing, CTRL-C to stop")
    # boucle sans fin -> CTRL-C pour terminer
    while True:
        # changer le status de la variable LED_status si 1 -> 0 si 0 -> 1
        LED_status = not LED_status
        # apliquer l'etat à la sortie
        GPIO.output(GPIO_channel_number,LED_status)
        # faire une pause pour que la fréquence de clignotment soir celle choisie
        time.sleep(LED_half_period)
        
except KeyboardInterrupt:
    print("bye")
    GPIO.output(GPIO_channel_number,LED_off)
    pass
