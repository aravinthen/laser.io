# Program Name: interface.py
# Author: Aravinthen Rajkumar
# Description:

import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

class Interface:
    """
    The gameplay is carried out via the interface.
    """
    def __init__(self,state, game):
        self.state = state
        self.game = game # this is used to interface with the full game object


