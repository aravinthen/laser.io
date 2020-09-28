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
# SHF [NUM1] [NUM2] - Shifts intensity from [NUM1] to [NUM2]
#
#
# TO ADD:
#   1) VARIABLES: DONE
#   2) FUNCTIONS: DONE
#   3) LOOPS: DONE
#   4) CONDITIONALS: DONE
#   5) ARITHMETIC: DONE
# 
# Meeting 1), 2) and 3) are the minimum for making the LASER CONTROL LANGUAGE Turing Complete.
##################################################################################################

class LaserControlLanguage:
    def __init__(self):
        # every command 
        self.program = ""
        self.variables = {}
        self.subroutines = {}

        # STATE OF PROGRAM
        self.intensity = 0
        self.angle = 0
        self.on = False

    def TURNON(self):
        """
        Appends symbol TON onto the program string
        """
        self.program += "TON\n"
        self.on = True
        

    def TURNOFF(self):
        """
        Appends symbol TOF onto the program string
        """
        self.program += "TOF\n"
        self.on = False

    def INTENSITY(self, value):
        """
        Sets an intensity value for the laser.
        """
        self.program += f"INT {value}\n"
        self.intensity = value

    def HOLD(self, value):
        """
        Holds the laser at it's position for a specified amount of time.
        """
        self.program += f"HOL {value}\n"

    def TURN(self, value, speed):
        """
        Turns the laser counterclockwise by a specified amount at a specified speed.
        """
        self.program += f"TRN {value} {speed}\n"
        self.angle += value
        self.angle = self.angle % 360

    def SHIFT(self, start, end):
        """
        Shifts intensity from start value to end.
        """
        self.program += f"SHF {start} {end}\n"
        self.intensity = end
        
    def DEF_VAR(self, var_name, var_val):
        self.variables[var_name] = var_val

    def DEF_SUBROUTINE(self, subspace, routine_name, *args):
        """
        Works by writing a program into another instance of the lcl
        """
        self.subroutines[routine_name] = subspace.program
        # need to reset subspace string
        subspace.program = ""
    
    def VAR(self, var_name):
        return self.variables[var_name]
    
    def SUBROUTINE(self, routine_name):
        self.program += self.subroutines[routine_name]
    
    def LOOP(self, subspace, repeat, *args):
        self.DEF_SUBROUTINE(subspace, "loop", args)      
        for i in range(repeat):
            self.program += self.subroutines["loop"]
        del self.subroutines["loop"]        

    def IF(self, VARIABLE, operation, value, func1, func2=None):
        # This depends on the state of the program. The states are:
        # INTENSITY, ANGLE , ON
        # These are the only options for the VARIABLE key.
        # ON must have "True" or "False" as the input
        
        # operation, on the other hand, is a keyholder for equality and inequalities. That is:
        # GT: >
        # LT: <
        # EQ: ==
        
        ops = {"GT": '>',
               "LT": '<',
               "EQ": '=='}
        
        com_satisfied = False
        
        # eval converts a string into a full program
        # it is extremely OP, pls nerf
        if VARIABLE == "INTENSITY":
            if eval("self.intensity" + ops[operation] + str(value)):                
                com_satisifed = True                
        elif VARIABLE == "ANGLE":
            if eval("self.angle" + ops[operation] + str(value)):
                com_satisifed = True
        elif VARIABLE == "ON":            
            if operation != "EQ":
                print("ERROR: INVALID SYNTAX")
                return 0
        
            if eval("self.on" + ops[operation] + str(value)):
                com_satisfied = True
        else:
            print("ERROR: INVALID COMMAND")

        
        if com_satisfied:
            self.SUBROUTINE(func1)
        else:
            if func2 != None:
                self.SUBROUTINE(func2)
                    
                
# ----------------------------------------------------------------------------------------------

lcl = LaserControlLanguage()
s = LaserControlLanguage()

lcl.DEF_VAR("init_intensity", 1000)
lcl.DEF_VAR("hold_time", 100)
lcl.DEF_VAR("turning_angle", 20)
lcl.DEF_SUBROUTINE(s, "blast", s.INTENSITY(10000), s.TURNON(), s.HOLD(10), s.TURNOFF())
lcl.DEF_SUBROUTINE(s, "megablast", s.INTENSITY(1000000), s.TURNON(), s.HOLD(10), s.TURNOFF())

lcl.INTENSITY(lcl.VAR("init_intensity"))

# lcl.LOOP(s, 10, s.TURNON(), s.HOLD(5), s.TURNOFF())

lcl.TURNON()
lcl.HOLD(lcl.VAR("init_intensity"))
lcl.TURNOFF()

lcl.IF("ON", "EQ", "True", "megablast", "blast")

lcl.TURN(lcl.VAR("turning_angle"), 2)
lcl.SUBROUTINE("megablast")

lcl.TURNON()
lcl.INTENSITY(100)
lcl.TURN(-20,3)
lcl.SHIFT(1000,0)

lcl.TURNOFF()

# print(lcl.program) # this will need to be parsed



