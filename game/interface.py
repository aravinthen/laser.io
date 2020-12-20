# Program Name: interface.py
# Author: Aravinthen Rajkumar
# Description:

import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

# Colours
BLUE = (106, 160, 184)
LBLUE = (0, 134, 143)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (128, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
NEONGREEN = (57, 255, 20)
RED = (255, 0, 0)

class Interface:
    """
    The gameplay is carried out via the interface.
    """    
    def __init__(self, game, ls):
        self.game = game # this is used to interface with the full game object
        self.ls = ls # allows access to laserscript features

        # NUM ENTRY FLAG:
        # this activates the calculator mode used to input numbers
        self.num_entry = False
        self.num = None # used to store a number that is inputted

    #--------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------
        
    def UpdateInterface(self,):
        pass
    
    def DrawInterface(self,):
        # The interface is intended to resemble an old-school terminal.
        # Black background, green text and buttons.
        # Have the words flashing across the screen as though they're being typed.
        self.game.display.fill(BLACK)
        pg.draw.line(self.game.display,
                     NEONGREEN,
                     (self.game.sx//2, 0),
                     (self.game.sx//2, self.game.sy))


