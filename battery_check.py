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
        
#Change the voltage to suit your needs here
    if (battery_state.battery_volts >= 3.63):
        Str = random.randint(1,3)
        print(Str)
        if Str==1:
                robot.behavior.say_text("Battery Great!!")
                
        if Str==2:
                robot.behavior.say_text("Voltage sufficent!!")
                
        if Str==3:
                robot.behavior.say_text("I'm all charged up!")
        
        #put your code to turn off your smart plug here
        #GPIO.output(17,GPIO.LOW)

#Change the voltage to suit your needs here, but make sure it is the same as the voltage above
    if (battery_state.battery_volts <= 3.63):
        Str = random.randint(1,3)
        print(Str)
        if Str==1:
                robot.behavior.say_text("Battery Low!!, turning on charger light")
                
        if Str==2:
                robot.behavior.say_text("Voltage Depleting!!, initialize charger light")
                
        if Str==3:
                robot.behavior.say_text("energize")
                
        #put your code to turn on your smart plug here
        #GPIO.output(17,GPIO.HIGH)
                
    #check if Vector is on his charger and turn off light if he is.
    if (battery_state.is_on_charger_platform == True):
        print("I'm on the charger!")
        #put your code to turn off your smart plug here
        #GPIO.output(17,GPIO.LOW)
