''' Auteurs   : Yannaël Métral et Anton Broggini
    Contact     : yannael.mtrl@eduge.ch et anton.brggn@eduge.ch
    License     : collégiens
    Librairie   : https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main
    Date        : 20 mai 2025
    Version     : 2
    Description : Robot qui reçoit le message pour partir faire le labyrinthe

   /''''^''''\
  /  L1 M R1  \
 |             |
 |L2         R2|
o|.............|o

'''
#Librairies
from maprincess import *
from microbit import *
import utime
from sendy import*

#Constantes
MOTOR_FORWARD = 0   #avant
MOTOR_BACKWARD = 1  #arrière
BLACK = 1   #détection line_sensor noir
WHITE = 0   #détection line_sensor blanc

#Variables
userId = 1  #numéro de l'utilisateur
depart = False #booléen pour executer au bon moment le départ

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

#Execution du programme
while True:
    if not depart:  #en attente du message pour partir 
        led_rgb(rgb(255,0,0))  #lumière rouge
        m = receive_msg(userId)
        if m and m.payload == [120]:
            print("Lesgoooo")
            depart = True
            led_rgb(rgb(0,128,0))
    else:
        led_rgb(rgb(255,255,255))  #lumière blanche pour mieux détecter les lignes
        # 3 sorties possibles: 1)mur noir devant = tourner à gauche
        #                      2)rien devant et mur à droite = avancer tout droit
        #                      3)rien devant et blanc à droite = tourner à droite
        compteur = running_time() #compteur début
        if line_sensor(LineSensor.M) == BLACK:
            tourne_d()
            avancer()
        elif line_sensor(LineSensor.L2) == BLACK:
            avancer()
        elif line_sensor(LineSensor.L2) == WHITE:
            tourne_g()
            avancer()
    if button_a.was_pressed(): 
        display.show(compteur)  #affiche le temps du parcours à la fin 
    if button_b.was_pressed():
        motor_stop(Motor.ALL) #arrête la bête
