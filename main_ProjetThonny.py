
''' Auteurs   : Yannaël Métral et Anton Broggini
    Contact     : yannael.mtrl@eduge.ch et anton.brggn@eduge.ch
    License     : collégiens
    Librairie   : https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main
    Date        : 26 mars 2025
    Version     : 1
    Description : 

   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''
from maprincess import *
from microbit import *
import utime

# Constantes
WHITE = 0
BLACK = 1
MOTOR_FORWARD = 0
MOTOR_BACKWARD = 1
# Variable globale
Init = True

def followLine(speed:int, speed_slow:int):
    ''' Fonction qui teste si on est sur la bande noire et commande les moteurs droite et gauche.
        Permet de rester sur une bande noire.
        params :
          speed (int) : vitesse donnée au(x) moteur(s). Pour tourner, le moteur le moins rapide sera speed-35
    '''
    # On teste si les capteurs infrarouge frontaux L1 et R1 détecte la bande noire
    if line_sensor(LineSensor.M)==BLACK:
        # On est sur la bande noire, on continue tout droit.
        print("On est sur la bande noir")
        display.show(Image.HAPPY)
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed)

    elif line_sensor(LineSensor.L1)==WHITE and line_sensor(LineSensor.R1)==BLACK:        
        # On est sorti à gauche, il faut revenir un peu sur la droite.
        print("Trop à gauche !")
        display.show("G")
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed_slow)

    elif line_sensor(LineSensor.L1)==BLACK and line_sensor(LineSensor.R1)==WHITE:
        # On est sorti à droite, il faut revenir un peu sur la gauche.
        # Le moteur gauche doit tourner moins vite que le moteur droit
        print("Trop à droite !")
        display.show("D")
        motor_run(Motor.LEFT, speed_slow)
        motor_run(Motor.RIGHT, speed )

    utime.sleep_ms(50)

while True:
    if Init:
        # Vitesse maximale des moteurs (min:0, max:255)
        speed:int = 70   #70
        speed_slow:int = 15 #15

        display.show("2")
        utime.sleep_ms(3000)
        Init = False
       
    print(line_sensor_all())
    if line_sensor(LineSensor.R2)==WHITE :
        motor_run(Motor.ALL, 70, MOTOR_FORWARD)
    else:
        motor_run(Motor.ALL, 0, MOTOR_FORWARD)
