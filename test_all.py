from __future__ import division
#import RPi.GPIO as gpio
import time
import curses
import Adafruit_PCA9685
import logging

pwm = Adafruit_PCA9685.PCA9685() #instaniate pulse-width modulation

#logging.basicConfig(level = logging.DEBUG)

#screen = curses.initscr()
#curses.noecho()
#curses.cbreak()
#screen.keypad(True)
#screen.nodelay(True)

servo_min = 150
servo_max = 900

#working frequency = 333hz
#new min = 100
#new max = 620

'''
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
'''
pwm.set_pwm_freq(60)


while True:
    #print('setting servos to min')
    #pwm.set_all_pwm(0, 0)
    for x in range(servo_min, servo_max):
        pwm.set_all_pwm(0, x)
        print(x)
        time.sleep(0.05)
    for y in range(servo_min, servo_max):
        pwm.set_all_pwm(0, ((servo_min+servo_max) - y))
        print(((servo_max+servo_min) -y))
        time.sleep(0.05)

    #pwm.set_pwm(0, 0, 0)
    #pwm.set_pwm(1, 0, 0)
    #time.sleep(0.5)
    #print('setting servos to max')
    #pwm.set_all_pwm(0, 100)
    #pwm.set_pwm(0, 0, 20)
    #pwm.set_pwm(1, 0, 20)
    #time.sleep(0.5)
