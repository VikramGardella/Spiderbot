from __future__ import division
import RPi.GPIO as gpio
import time
import curses
import Adafruit_PCA9685
import logging

pwm = Adafruit_PCA9685.PCA9685() #instaniate pulse-width modulation for servo driver

#logging.basicConfig(level = logging.DEBUG)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.nodelay(True)

servo_min = 100
servo_med = 360
servo_max =  620
servo_curr = 360

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    pulse_length //= 4096
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)



limb_names = ['front_left', 'front_right', 'back_left', 'back_right']
limb_motor_channels = [[0, 1, 2], [15, 14, 13], [3, 4, 5], [12, 11, 10]]
limb_index = 0

try:
    while True:
        char = screen.getch()
        if(char != -1):
            #switch leg to manipulate
            if(char == ord('u')):
                limb_index = 0
                print('Now controlling front left leg.')
            elif(char == ord('i')):
                limb_index = 1
                print('Now controlling front right leg.')
            elif(char == ord('j')):
                limb_index = 2
                print('Now controlling back left leg.')
            elif(char == ord('k')):
                limb_index = 3
                print('Now controlling back right leg.')
            #top joint
            elif(char == ord('q')):
                servo_curr -= 10
                print('servo_curr = %d' % servo_curr)
                pwm.set_pwm(limb_motor_channels[limb_index][0], 0, servo_curr)
            elif(char == ord('w')):
                print('setting servo signal to 360')
                pwm.set_pwm(limb_motor_channels[limb_index][0], 0, servo_med)
            elif(char == ord('e')):
                servo_curr += 10
                print('servo_curr = %d' %  servo_curr)
                pwm.set_pwm(limb_motor_channels[limb_index][0], 0, servo_curr)
            #middle joint
            elif(char == ord('a')):
                pwm.set_pwm(limb_motor_channels[limb_index][1], 0, servo_min)
            elif(char == ord('s')):
                pwm.set_pwm(limb_motor_channels[limb_index][1], 0, servo_med)
            elif(char == ord('d')):
                pwm.set_pwm(limb_motor_channels[limb_index][1], 0, servo_max)
            #bottom joint
            elif(char == ord('z')):
                pwm.set_pwm(limb_motor_channels[limb_index][2], 0, servo_min)
            elif(char == ord('x')):
                pwm.set_pwm(limb_motor_channels[limb_index][2], 0, servo_med)
            elif(char == ord('c')):
                pwm.set_pwm(limb_motor_channels[limb_index][2], 0, servo_max)
            else:
                print('Clean signal to servo driver here.')


except KeyboardInterrupt:
    terminate()

finally:
    terminate()

