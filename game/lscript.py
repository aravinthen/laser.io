# Program Name: 
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
    def __init__(self, state, game):
        self.state = state
        self.game = game # this is used to interface with the full game object
