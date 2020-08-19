# Program Name: lasercontrollang.py
# Author: Aravinthen Rajkumar
# Description: This is a rudimentary parser for a very basic "programming language".
#              It translates a set of commands into a string that will then be read to control
#              a graphical "laser". Essentially, the string represents a program in it's
#              machine code form. 
#              The commands themselves are functions that modify the "program" string in some
#              way.
#              The hope is that this will become a cooler version of the typical "control a
#              robot and draw some circles" introductory program, with a bit of leeway to
#              teach users about rudimentary scientific models and statistics.

##################################################################################################
# LASER CONTROL LANGUAGE - SYNTAX
# Every command Takes the form of THREE LETTERS FOLLOWED BY A NUMBER IF PERMITTED.
#
# TON               - Turns laser ON
# TOF               - Turns laser OF(F)
# INT [NUM]         - Sets an "INTensity" for the laser. This will be something like
#                     "the number of particles fired from the laser per timestep."
# HOL [NUM]         - HOLds the laser in it's current position for a number of timesteps.
# TRN [NUM1] [NUM2] - Turns the laser by a specified amount at one of five speeds. [NUM2] must be
#                     an integer.
# SHF [NUM1] [NUM2] - Shifts intensity from 
##################################################################################################


class LaserControlLanguage:
    def __init__(self):
        # every command 
        self.program = ""

    def TURNON(self):
        """
        Appends symbol TON onto the program string
        """
        self.program += "TON\n"
        

    def TURNOFF(self):
        """
        Appends symbol TOF onto the program string
        """
        self.program += "TOF\n"

    def INTENSITY(self, value):
        """
        Sets an intensity value for the laser.
        """
        self.program += f"INT {value}\n"

    def HOLD(self, value):
        """
        Holds the laser at it's position for a specified amount of time.
        """
        self.program += f"HOL {value}\n"

    def TURN(self, value, speed):
        """
        Turns the laser by a specified amount at a specified speed.
        """
        self.program += f"TRN {value} {speed}\n"

    def SHIFT(self, start, end):
        """
        Turns the laser by a specified amount at a specified speed.
        """
        self.program += f"SHF {start} {end}\n"

lcl = LaserControlLanguage()
lcl.INTENSITY(1000)
lcl.TURNON()
lcl.HOLD(100)
lcl.TURNOFF()
lcl.TURN(20, 2)
lcl.INTENSITY(100)
lcl.TURN(-20,3)
lcl.SHIFT(1000,0)
lcl.TURNOFF()

print(lcl.program)
    


