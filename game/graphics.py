# Program Name: lmechanics.py
# Author: Aravinthen Rajkumar
# Description:
import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

# colours
BLUE = (106, 160, 184)
LBLUE = (0, 134, 143)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (128, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)

class Graphics:    
    # ---------------------------------------- LASER  -----------------------------------------
    class Laser:
        """
        The laser is drives the interaction process. It assumes the following processes:
        - state:        on or off
        - position:     the point at which the laser is fired
        - angle:        the orientation of the laser
        - intensity:    the power of the laser (will be used to control ablation rate)
        - energy:       the amount of energy the laser has: powers down when energy is spent
        """
        def __init__(self,):
            """
            Initialise laser, relevant data (the position, orientation, intensity, state, and 
            energy).
            """
            pass
        
        
        def update_laser(self,):
            """
            Updates the state of the laser variables.
            If the laser's state variable is True, a line will be drawn. 
            """
            pass
        
    # ---------------------------------------- MATERIALS -----------------------------------------
    class Materials:
        """
        There are two kinds of materials used in the game.
          a) Material particles that interact with the laser.
             These are given two position values, x and y.
          b) Gas particles, which are formed in two situations:
             - When the material comes into contact with a laser.
             - When a gas particle comes into contact with a material.
             Gas particles take velocity values as well as position values.
            
          The particles are stored into separate lists, which are then acted on via the update
          function.
        """
        
        def __init__(self,):
            """
            Initialise material lists and relevant details.
            """
            pass
            
        def structure(self,):
            """
            This function is used to build structures.
            This should only be used once as an initialisation function.
            """
            pass
    
        def update_material(self):
            """
            Updates the state of all of the gas and solid objects in ther materials class.
            Solids that become gas particles are deleted from the solids list and put into
            the gas list, with random values for velocity added too.
            """
            pass

# -------------------------------------------------------------------------------------------------

    def __init__(self, game, ls):
        self.game = game   # allows access to the whole game object
        self.ls = ls       # allows access to laserscript features
                           # the main features needed in this section is the parser,
                           # which will convert the instructions specified in the
                           # interface into animations.

    def scoring(self,):
        """
        This is used to compare the CURRENT state of the material to the GOAL state.
        The Goal state will have been set in the menu.
        """
        pass
        
    def UpdateGraphics(self,):
        pass
    
    def DrawGraphics(self,):
        self.game.display.fill(WHITE)
