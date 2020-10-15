# Program Name: laser_animation.py
# Author: 
# Description:

import pygame as pg
import os

class Laser:
    def __init__(self,):
        # polar angle to specify position on a circle
        # default position is held to be at the very bottom of the circle
        self.theta = 270
        
        # angle spefifies orientiation of laser
        self.angle = 90

        self.status = False # laser is turned off by default
        self.laserImg = pg.image.load('laser_images/monster.png')

        

class Pixel:
    def __init__(self, x, y, intensity):
        self.x = x
        self.y = y
        self.intensity = intensity # set this to zero for non-laser type pixels
