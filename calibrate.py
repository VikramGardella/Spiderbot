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

#servo_fl = 1250
#servo_fr = 700
#servo_bl = 700
#servo_br = 1250

limb_names = ['front_left', 'front_right', 'back_left', 'back_right']
limb_motor_channels = [[0, 1, 2], [15, 14, 13], [3, 4, 5], [12, 11, 10]]
limb_index = 0
top_motor_sigs = [1250, 700, 700, 1250]
#mid_motor_sigs = [?, ?, ?, ?]
#bot_motor_sigs = [?, ?, ?, ?]

try:
    while True:
        char = screen.getch()
        if(char != -1):
            #switch leg to manipulate
            if(char == ord('u')):
                limb_index = 0
                servo_curr = 360
                print('Now controlling front left leg.')
            elif(char == ord('i')):
                limb_index = 1
                servo_curr = 360
                print('Now controlling front right leg.')
            elif(char == ord('j')):
                limb_index = 2
                servo_curr = 360
                print('Now controlling back left leg.')
            elif(char == ord('k')):
                limb_index = 3
                servo_curr = 360
                print('Now controlling back right leg.')
            #top joint
            elif(char == ord('q')):
                #servo_curr -= 10
                print('servo_curr = %d' % top_motor_sigs[limb_index])
                #pwm.set_pwm(limb_motor_channels[limb_index][0], 0, servo_curr)
                top_motor_sigs[limb_index] -= 10
            elif(char == ord('w')):
                print('setting servo signal to 360')
                #pwm.set_pwm(limb_motor_channels[limb_index][0], 0, servo_med)
                #top_motor_sigs[limb_index] =
            elif(char == ord('e')):
                #servo_curr += 10
                print('servo_curr = %d' % top_motor_sigs[limb_index])
                #pwm.set_pwm(limb_motor_channels[limb_index][0], 0, servo_curr)
                top_motor_sigs[limb_index] += 10
            elif(char == ord('t')):
                print('setting motor positions for installing top limbs')
                #pwm.set_pwm(limb_motor_channels[0][0], 0, 1220) #front left
                #pwm.set_pwm(limb_motor_channels[1][0], 0, 700) #front right
                #pwm.set_pwm(limb_motor_channels[2][0], 0, 700) #back left
                #pwm.set_pwm(limb_motor_channels[3][0], 0, 1220) #back right
                top_motor_sigs[0] = 1250
                top_motor_sigs[1] = 700
                top_motor_sigs[2] = 700
                top_motor_sigs[3] = 1250
            elif(char == ord('o')):
                #make legs go out
                print('legs out')
                top_motor_sigs[0] = 900
                top_motor_sigs[1] = 1050
                top_motor_sigs[2] = 1050
                top_motor_sigs[3] = 900

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

            pwm.set_pwm(limb_motor_channels[0][0], 0, top_motor_sigs[0])
            pwm.set_pwm(limb_motor_channels[1][0], 0, top_motor_sigs[1])
            pwm.set_pwm(limb_motor_channels[2][0], 0, top_motor_sigs[2])
            pwm.set_pwm(limb_motor_channels[3][0], 0, top_motor_sigs[3])


except KeyboardInterrupt:
    terminate()

finally:
    terminate()

