#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

# センサーのインスタンスの生成
CS1 = ColorSensor(PortS1)
CS2 = ColorSensor(PortS2)
CS3 = ColorSensor(PortS3)
CS4 = ColorSensor(PortS4)

TS_left = TouchSensor(portS)
TS_right = TouchSensor(portS)

# モーターのインスタンスの生成
left_motor = Motor(port)
right_motor = Motor(port)

# 定義
black_hightest_refrection = 10
silber_lowest_refrection = 40
Kp = 1.5
Ki = 0.5
Kd = 1.3
individual_difference = 0 #cs2-cs3　個体差

turn90 = 0
turn180 = 0
#ここまでは事前にやっとく
errors = [0,0,0,0,0]

informations_return = []

#ボタン入力があるまで待機
while not any(ev3.buttons.pressed()):
    wait(10)

line()