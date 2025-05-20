''' Auteurs   : Yannaël Métral et Anton Broggini
    Contact     : yannael.mtrl@eduge.ch et anton.brggn@eduge.ch
    License     : collégiens
    Librairie   : https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main
    Date        : 20 mai 2025
    Version     : 2.1
    Description :

   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''

#Librairies
from maprincess import *
from microbit import *
#Constantes
MOTOR_FORWARD = 0   #avant
MOTOR_BACKWARD = 1  #arrière
BLACK = 1   #détection line_sensor noir
WHITE = 0   #détection line_sensor blanc

#Instruction
led_rgb(rgb(255,255,255))   #lumière blanche pour mieux détecter les lignes

#Définitions
def avancer():    #fonction pour avancer
    motor_run(Motor.ALL, 40, MOTOR_FORWARD)
    sleep(100)
    motor_stop(Motor.ALL)
   
def tourne_d():   #fonction pour tourner à droite
    motor_run(Motor.LEFT, 90, MOTOR_FORWARD)
    motor_run(Motor.RIGHT, 110, MOTOR_BACKWARD)
    sleep(220)
    motor_stop(Motor.ALL)
   
def tourne_g():   #fonction pour tourner à gauche
    motor_run(Motor.RIGHT, 90, MOTOR_FORWARD)
    motor_run(Motor.LEFT, 110, MOTOR_BACKWARD)
    sleep(220)
    motor_stop(Motor.ALL)

#Boucle True
while True:
    # 3 sorties possibles: 1)mur noir devant = tourner à gauche
    #                      2)rien devant et mur à droite = avancer tout droit
    #                      3)rien devant et blanc à droite = tourner à droite
    if line_sensor(LineSensor.M) == BLACK:
        tourne_g()
        avancer()
    elif line_sensor(LineSensor.R2) == BLACK:
        avancer()
    elif line_sensor(LineSensor.R2) == WHITE:
        tourne_d()
        avancer()
