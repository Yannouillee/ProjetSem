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
V1 = True
V2 = True
led_rgb(rgb(255,255,255))
# Variable globale
Init = True
c = [] #liste colone
l = [] #liste ligne
d = "E" # direction (E/O/N/S)
x = 22
y = 16

def followLine(speed:int, speed_slow:int):
    ''' Fonction qui teste si on est sur la bande noire et commande les moteurs droite et gauche.
        Permet de rester sur une bande noire.
        params :
          speed (int) : vitesse donnée au(x) moteur(s). Pour tourner, le moteur le moins rapide sera speed-35
    '''
    # On teste si les capteurs infrarouge frontaux L1 et R1 détecte la bande noire
    if 40 < line_sensor_data(LineSensor.M) < 210:
        # On est sur la bande noire, on continue tout droit.
        print("On est sur la bande noir")
        display.show(Image.HAPPY)
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed)

    elif line_sensor(LineSensor.L1)==WHITE and 40 < line_sensor_data(LineSensor.R1) < 210:        
        # On est sorti à gauche, il faut revenir un peu sur la droite.
        print("Trop à gauche !")
        display.show("G")
        motor_run(Motor.LEFT, speed)
        motor_run(Motor.RIGHT, speed_slow)

    elif 40 < line_sensor_data(LineSensor.L1) < 210 and line_sensor(LineSensor.R1)==WHITE:
        # On est sorti à droite, il faut revenir 40 < line_sensor_data(LineSensor.R1) < 210un peu sur la gauche.
        # Le moteur gauche doit tourner moins vite que le moteur droit
        print("Trop à droite !")
        display.show("D")
        motor_run(Motor.LEFT, speed_slow)
        motor_run(Motor.RIGHT, speed )

    utime.sleep_ms(50)
    
def tourne_d(speed):
    sleep(100)
    motor_run(Motor.LEFT, speed, MOTOR_FORWARD)
    motor_run(Motor.RIGHT, speed_slow, MOTOR_BACKWARD)
    sleep(750)
    
def tourne_g(speed):
    sleep(100)
    motor_run(Motor.RIGHT, speed, MOTOR_FORWARD)
    motor_run(Motor.LEFT, speed_slow, MOTOR_BACKWARD)
    sleep(720)

def cr_d(speed_slow):
    sleep(100)
    motor_run(Motor.RIGHT, 15, MOTOR_BACKWARD)
    motor_run(Motor.LEFT, 15, MOTOR_BACKWARD)
    sleep(50)
    tourne_d(speed)
    sleep(100)

    if d == "N":
        d = "E"
    elif d == "E":
        d = "S"
    elif d == "S":
        d = "O"
    elif d == "O":
        d = "N"
        
def cr_g(speed_slow):
    motor_run(Motor.RIGHT, 15, MOTOR_BACKWARD)
    motor_run(Motor.LEFT, 15, MOTOR_BACKWARD)
    sleep(50)
    tourne_g(speed)
    sleep(100)
    if d == "N":
        d = "O"
    elif d == "O":
        d = "S"
    elif d == "S":
        d = "E"
    elif d == "E":
        d = "N"
        
while True:
    if Init:
        # Vitesse maximale des moteurs (min:0, max:255)
        speed:int = 70   #70
        speed_slow:int = 25 #15

        display.show("2")
        utime.sleep_ms(3000)
        Init = False
#     if line_sensor(LineSensor.R2) == BLACK and line_sensor(LineSensor.L1) == WHITE:
#         motor_run(Motor.ALL, 30, MOTOR_FORWARD)
#     else:
#         motor_run(Motor.ALL, 0, MOTOR_FORWARD)
#     if line_sensor(LineSensor.L1) == BLACK:
#         motor_run(Motor.RIGHT, 40, MOTOR_FORWARD)
#     else:
#         motor_run(Motor.ALL, 0, MOTOR_FORWARD)
#     if line_sensor(LineSensor.R2) == WHITE:
#         motor_run(Motor.LEFT, 30, MOTOR_FORWARD)

    elif line_sensor(LineSensor.L2) == BLACK:
        motor_run(Motor.LEFT, 40, MOTOR_FORWARD)
    else:
        motor_run(Motor.ALL, 20, MOTOR_FORWARD)
#     print(line_sensor_all())
#     if line_sensor_data(LineSensor.M) > 50 and line_sensor_data(LineSensor.R2) < 20 and line_sensor_data(LineSensor.R1) >50 : #and V1 == True:
#         motor_run(Motor.ALL, 50, MOTOR_FORWARD)
#     elif line_sensor_data(LineSensor.M) < 50:
#         cr_g(speed_slow)
#     else:
#         motor_run(Motor.ALL, 50, MOTOR_FORWARD)


    if 40 < line_sensor_data(LineSensor.R1) < 210:
    #def gauche pu droite change le d pour connaitre l'orientation
        sleep(200)
        if d == "N":
            x -= 1    
        elif d == "E":
            y -= 1
        elif d == "O":
            y += 1
        elif d == "S":
            x += 1
        print("x:", x, "y:", y)
        
#     if line_sensor(LineSensor.R2)==BLACK :
#         motor_run(Motor.ALL, 70, MOTOR_FORWARD)
#     else:
#         motor_run(Motor.ALL, 0, MOTOR_FORWARD)
    
    
    