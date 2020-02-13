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

servo_min = 100
servo_med = 360
servo_max =  620

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    pulse_length //= 4096
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

#pwm.set_pwm_freq(60)

limb_names = ['front_left', 'front_right', 'back_left', 'back_right']
limb_motor_channels = [[0, 1], [2, 3], [4, 5], [6, 7]]
camera_motor_channel = 15

def limb_cont(limb_name, percent):
    print('Setting contraction of the %s limb to %d percent' % (limb_name, percent))
    print('Limb motor channels being used are: %d and %d' % (limb_names[limb_name][0], limb_names[limb_name][1]))

def move_for():
    print('Moving forward.')

def move_back():
    print('Moving backward.')

def move_left():
    print('Moving leftward.')

def move_right():
    print('Moving rightward.')

def rot_body_left():
    print('Rotating left.')

def rot_body_right():
    print('Rotating right.')

def stand_up():
    print('Standing up')

def sit_down():
    print('Sitting down.')

def rot_cam_left():
    print('Rotating camera left.')

def rot_cam_right():
    print('Rotating camera right.')


try:
    while True:
        char = screen.getch()
        if(char != -1):
            if(char == ord('q')):
                pwm.set_pwm(0, 0, servo_min)
            elif(char == ord('a')):
                pwm.set_pwm(0, 0, servo_med)
            elif(char == ord('z')):
                pwm.set_pwm(0, 0, servo_max)
            elif(char == ord('w')):
                pwm.set_pwm(1, 0, servo_min)
            elif(char == ord('s')):
                pwm.set_pwm(1, 0, servo_med)
            elif(char == ord('x')):
                pwm.set_pwm(1, 0, servo_max)
            elif(char == ord('e')):
                pwm.set_pwm(2, 0, servo_min)
            elif(char == ord('d')):
                pwm.set_pwm(2, 0, servo_med)
            elif(char == ord('c')):
                pwm.set_pwm(2, 0, servo_max)
            elif(char == ord('r')):
                pwm.set_pwm(3, 0, servo_min)
            elif(char == ord('f')):
                pwm.set_pwm(3, 0, servo_med)
            elif(char == ord('v')):
                pwm.set_pwm(3, 0, servo_max)
            else:
                print('Clean signal to servo driver here.')


except KeyboardInterrupt:
    terminate()

finally:
    terminate()

