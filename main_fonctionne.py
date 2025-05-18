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

MOTOR_FORWARD = 0
MOTOR_BACKWARD = 1
BLACK = 1
WHITE = 0
led_rgb(rgb(255,255,255))
# Variable globale


def avancer():
    motor_run(Motor.ALL, 40, MOTOR_FORWARD)
    sleep(100)
    motor_stop(Motor.ALL)
   
def tourne_d():
    motor_run(Motor.LEFT, 110, MOTOR_FORWARD)
    motor_run(Motor.RIGHT, 110, MOTOR_BACKWARD)
    sleep(220)
    motor_stop(Motor.ALL)
   
def tourne_g():
    motor_run(Motor.RIGHT, 110, MOTOR_FORWARD)
    motor_run(Motor.LEFT, 110, MOTOR_BACKWARD)
    sleep(220)
    motor_stop(Motor.ALL)


while True:
    
    if line_sensor(LineSensor.M) == BLACK:
        tourne_g()
        avancer()
    elif line_sensor(LineSensor.R2) == BLACK:
        avancer()
    elif line_sensor(LineSensor.R2) == WHITE:
        tourne_d()
        avancer()
