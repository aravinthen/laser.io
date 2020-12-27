# Program Name: game_file.py
# Description: The complete file for the full hetsys game

import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

# program-specific subclasses
from menu import Menu
from interface import Interface
from graphics import Graphics

class LaserGame:
#-------------------------------------------------------------------------------------------------
#                                        GENERAL USER INTERFACE
# This part of the code is dedicated to the CONTROL of the game: that is, the input.
# It will contain the starting menu, the programming interface and the full laser script language.
# The Laserscript language will be taken as input for the MECHANICS section, which will produce 
# the laser ablation animations.
#-------------------------------------------------------------------------------------------------

    # ----------------------------------------- GAME FUNCTIONS -----------------------------------
    # Note: these methods are applied to the full LaserGame object.
    # Overall though, as a design choice, they're extremely simple. The bulk of the methods will
    # simply call methods assigned to other objects.
    def Draw(self,):
        """
        Takes everything from the above and draws it onto the relevant screen.
        """
        if self.mode == "menu":
            self.menu.DrawMenu()
            
        if self.mode == "interface":
            self.interface.DrawInterface()

        if self.mode == "graphics":
            self.graphics.DrawGraphics()


    def Update(self,):
        """
        Will be used to carry out all updates.
        """
        if self.mode == "menu":
            # All methods relating to updating the menu will be called here.
            self.menu.UpdateMenu()
            
        if self.mode == "interface":
            self.interface.UpdateInterface()

        if self.mode == "graphics":
            self.graphics.UpdateGraphics()

            
        pg.display.update()        
    
    def __init__(self, sizex, sizey, framerate):
        """
        Here is where the full game is initialized.
        Everything to do with the actual running of the game goes in here: Pygame, game metadata,
        and the parameters needed to make different parts of the game interact with eachother.
        sizex: length of game box in x-dimension
        sizey: length of game box in y-dimension
        framer: the framerate.
        """
        self.sx = sizex
        self.sy = sizey
        self.framerate = framerate

        # Pygame specific details
        self.clock = pg.time.Clock()
        
        # If you want to draw, draw to the display.
        self.display = pg.display.set_mode((sizex,sizey))
        # Might want to change this later on.
        pg.display.set_caption("laser.io")

        # The objects required to play the game are initialised all together.
        # the second "self" variable is used to access the full LaserGame object from
        # the menu and interface classes.
        # REMEMBER! LOWER CASE: the INITIALISED object
        #           UPPER CASE: the CLASS object
        # In most cases, you should be calling the initialised object.
                
        # menu screen
        self.menu = Menu(self)
        self.level = None # this is set by the user within the menu.

        # these are the components of the game itself
        # interface:  the section where the player controls the game: input
        # graphics:   the output of the interface.
        # ls:         Contains the laserscript language as well as a parser to
        #             control the output
        
#        self.ls = LaserScript(self) # key module, a bridge between interface
                                                # and the output.
        self.interface = Interface(self,)
        self.graphics = Graphics(self,)

        self.mode = "menu" # This controls the game mode that the player is currently in.
                           # It is updated on the fly.
                           # Possible modes:  1. menu
                           #                  2. interface
                           #                  3. graphics
                           
        
        pg.init() # initialize pygame
        finished = False
        while not finished:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print("Thank you for playing!")
                    print("Still to do: 1. Scale fonts with size.")
                    print("             2. ...")
                    finished = True
            self.Draw()   # fill in the screen
            self.Update() # all of the data updates are wrapped up in this function.

            self.clock.tick(self.framerate) # increases the clock by the number of frames
                                            # specified
        
        pg.quit()
        
#--------------------------------------------------------------------------------------------

# The basic control flow of a game is:
# Initialise the Game object.
#   While game is running:
#     Draw the current scene.
#     Update variables.
#     Check the new inputs
#      Repeat

LaserGame(800, 600, 30)
