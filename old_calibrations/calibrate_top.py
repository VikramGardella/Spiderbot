from __future__ import division
import RPi.GPIO as gpio
import time
import curses
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685() #instaniate pulse-width modulation for servo driver

#logging.basicConfig(level = logging.DEBUG)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)

servo_min = 160
servo_med = 270
servo_max = 380

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    pulse_length //= 4096
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

#pwm.set_pwm_freq(60)

limb_names = ['front_left', 'back_left', 'front_right',  'back_right']
limb_motor_channels = [[0, 1, 2], [3, 4, 5], [15, 14, 13], [12, 11, 10]]


try:
    while True:
        char = screen.getch()
        if(char != -1):
            if(char == ord('q')): #front left motor
                pwm.set_pwm(0, 0, servo_min)
            elif(char == ord('a')):
                pwm.set_pwm(0, 0, servo_med)
            elif(char == ord('z')):
                pwm.set_pwm(0, 0, servo_max)
            elif(char == ord('w')): #back left motor
                pwm.set_pwm(3, 0, servo_min)
            elif(char == ord('s')):
                pwm.set_pwm(3, 0, servo_med)
            elif(char == ord('x')):
                pwm.set_pwm(3, 0, servo_max)
            elif(char == ord('e')): #front right motor
                pwm.set_pwm(15, 0, servo_min)
            elif(char == ord('d')):
                pwm.set_pwm(15, 0, servo_med)
            elif(char == ord('c')):
                pwm.set_pwm(15, 0, servo_max)
            elif(char == ord('r')): #back right motor
                pwm.set_pwm(12, 0, servo_min)
            elif(char == ord('f')):
                pwm.set_pwm(12, 0, servo_med)
            elif(char == ord('v')):
                pwm.set_pwm(12, 0, servo_max)
            else:
                print('Clean signal to servo driver here.')
            #time.sleep(0.06)

except KeyboardInterrupt:
    terminate()

finally:
    terminate()
