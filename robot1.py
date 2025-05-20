''' Auteurs   : Yannaël Métral et Anton Broggini
    Contact     : yannael.mtrl@eduge.ch et anton.brggn@eduge.ch
    License     : collégiens
    Librairie   : https://github.com/GBSL-Informatik/maqueen-plus-v2-mpy/tree/main
    Date        : 20 mai 2025
    Version     : 3
    Description : Robot qui fait en premier le parcours, puis qui envoie dès la détection d'un objet avec l'utrason un message au deuxième robot pour partir, finalement joue la musique 

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
import music

#Constantes
MOTOR_FORWARD = 0   #avant
MOTOR_BACKWARD = 1  #arrière
BLACK = 1   #détection line_sensor noir
WHITE = 0   #détection line_sensor blanc
music.set_tempo(ticks=4, bpm = 124) #4 temps par mesure, 124 battements par minute
#Instruction
led_rgb(rgb(255,255,255))   #lumière blanche pour mieux détecter les lignes

#Variables
userId = 0  #numéro de l'utilisateur
destId = 1  #numéro de l'expéditeur
Mur_Trouve = False  #booléen pour executer au bon moment l'envoie
time0 = running_time()  #démarage du temps pour avoir la référence zéro

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

#Musique
FINAL_COUNTDOWN = ["F#2:1", "C#3:1", "F#3:4", "C#5:1", "B4:1", "C#5:4", "F#4:4", "D2:1", "A2:1", "D3:4", "D5:1", "C#5:1", "D5:2", "C#5:2", "B4:4", "B1:1", "F#2:1", "B2:4", "D5:1", "C#5:1", "D5:4", "F#4:4",
                   "E2:1", "B2:1", "G#3:4", "B4:1", "A4:1", "B4:2", "A4:2", "G#4:2", "B4:2", "A4:2", "F#2:1", "C#3:1", "F#3:2", "C#5:1", "B4:1", "C#5:4", "F#4:4", "D2:1", "A2:1", "D3:4", "D5:1", "C#5:1", "D5:2",
                   "C#5:2", "B4:4", "B1:1", "F#2:1", "B2:4", "D5:1", "C#5:1", "D5:4", "F#4:4",
                   "E2:1", "B2:1", "G#3:4", "B4:1", "A4:1", "B4:2", "A4:2", "G#4:2", "B4:2", "A4:1", "A3:1", "C#4:1", "E4:1", "A3:1", "E3:1", "G#4:1", "A4:1", "B4:1", "B2:1", "E3:1", "G#3:1", "B3:1", "G#3:1", "A4:1", "B4:1",
                   "C#5:2", "B4:2", "A4:2", "G#4:2", "F#4:1", "F#3:1", "F#4:1", "F#3:1", "D5:1", "F#4:1", "D5:1", "F#4:1", "C#5:1", "G#4:1", "F4:1", "C#4:1", "G#3:1", "F3:1", "C#3:1", "G#2:1", "F2:1", "C#2:2"]

#Execution du programme
while True:
    while not Mur_Trouve: # pour sortir de la boucle à la fin du labyrinthe
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
        
        time1 = running_time()  # vérifie que le delta du temps est supérieur à une seconde pour vérifier l'ultrason
        if time1 - time0 > 1000:
            time0 = time1
            if 2 < ultrasonic() < 15:   # si un objet est détecté, un message est envoyé à l'autre robot
                send_msg(1,[120],userId, destId)
                Mur_Trouve = True
                print("fin")
                motor_stop(Motor.ALL)
                led_rgb(rgb(0,128,0))
    music.play(FINAL_COUNTDOWN)