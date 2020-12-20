# Program Name: lscript.py
# Author: Aravinthen Rajkumar
# Description: 

import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

class LaserScript:
    """
    This is the scripting lanuage that the player will use to control the laser.
    It will be used alongside the interface to generate the input.
    """
    def __init__(self, game):
        self.game = game # this is used to interface with the full game object

        # The program developed by the user will be stored in this string.        
        self.program = ""



    def intEnt(self, index):
        # int(erface)ent(ry)
        # The buttons in the interface map to a number in this function.
        # When the function is called with a relevent number as an input, the matching command
        # is stored onto the "self.program" string.
        # The parsing of the self.program string will be done in a separate function.
        
        # Of the commands, 3, 4, 5 and 6 will activate the self.num flag.
        # See line 23 for details on how this is used.
        
        commands = {1: "TON", # turn on laser beam.
                    2: "TOF", # turn off laser beam.
                    3: "PSE", # PauSE: Pause the program for N seconds
                    4: "INT", # set intensity.
                    5: "FRT", # Full RoTation: rotates the laser about the center of the screen
                    6: "ORT", # ORienT: Orients the laser about it's midpoint
                    7: "SFR", # Start FoR loop. 
                    8: "EFR", # End FoR loop.
                              # will probably need to be augmented to include variables
                    }

        if index in (3, 4, 5, 6, 7, 8):
            num = self.numEnt()
            self.program += f"{commands[index]} {num}"
        else:
            self.program += commands[index]

    def numEnt(self,):
        # allows the user to input numbers
        self.game.interface.num_entry = True
        
        # ----------------------------------------------------------------------
        # Number is inputted via the interface
        # This is completely controlled via the interface
        # ----------------------------------------------------------------------
        
        output = self.game.interface.num
        self.game.interface.num_entry = False
        self.game.interface.num = None        
        return output
    
    def backspace(self, ):
        # used to delete a line from the program
        pass
    
    def graPar(self,):
        # gra(phics)Par(sing)
        # This function translates the program assembled through the interface entry function
        # into the relevant animations for the graphics.
        
        # Also serves a vital purpose of throwing up errors.
        
        # NOTE: to access the initialized graphics object, use:
        #    game.graphics.{variable}.        
        pass


