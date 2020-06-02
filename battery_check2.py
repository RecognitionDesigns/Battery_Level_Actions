#!/usr/bin/env python3

import threading

import anki_vector
import random
import os

with anki_vector.Robot() as robot:
    battery_state = robot.get_battery_state()
    if battery_state:
        print("Robot battery voltage: {0}".format(battery_state.battery_volts))
        print("Robot battery Level: {0}".format(battery_state.battery_level))
        print("Robot battery is charging: {0}".format(battery_state.is_charging))
        print("Robot is on charger platform: {0}".format(battery_state.is_on_charger_platform))

    if (battery_state.battery_volts >= 3.63):
        Str = random.randint(1,3)
        print(Str)
        if Str==1:
                robot.behavior.say_text("Battery Great!!")
                
        if Str==2:
                robot.behavior.say_text("Voltage sufficent!!")
                
        if Str==3:
                robot.behavior.say_text("I'm all charged up!")
                
        Str = random.randint(4,6)
        if Str==4:
                robot.behavior.say_text("turning on charger light!!")
                
        if Str==5:
                robot.behavior.say_text("light it up!!")
                
        if Str==6:
                robot.behavior.say_text("energize")
                
        os.system("cd ~/vector_sdk/ && ./codesend 3553014 -l 400")

    if (battery_state.battery_volts <= 3.63):
        Str = random.randint(1,2)
        print(Str)
        if Str==1:
                robot.behavior.say_text("Battery Low!!, turning on charger light")
                GPIO.output(17,GPIO.HIGH)
        if Str==2:
                robot.behavior.say_text("Voltage Depleting!!, initialize charger light")
                GPIO.output(17,GPIO.HIGH)
                
    #check if Vector is on his charger and turn off light if he is.

    if (battery_state.is_on_charger_platform == True):
        print("I'm on the charger!")
        GPIO.output(17,GPIO.LOW)