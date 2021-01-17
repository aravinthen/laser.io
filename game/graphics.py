# Program Name: lmechanics.py
# Author: Aravinthen Rajkumar
# Description:
import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import time

import math as m
import os

# colours
BLUE = (106, 160, 184)
DBLUE = (0, 0, 128)
LBLUE = (0, 134, 143)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (128, 255, 0)
NEONGREEN = (57, 255, 20)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)

# import the materials
from materials import Laser, Materials

class Graphics:    
# -------------------------------------------------------------------------------------------------

    def __init__(self, game):
        self.game = game   # allows access to the whole game object
        self.sleep_time = 0.05
        
        self.backpos = (0.03*self.game.sx, 0.93*self.game.sy)
        self.hback = 0.08*self.game.sx
        self.vback = 0.05*self.game.sy
        
        # The specifications of the grid
        
        self.reference = 0.9*min([self.game.sx, self.game.sy])
        self.game_unit = self.reference/100 # the in-game units, instead of pixels        
        self.xcoord = 0.5*(max([self.game.sx, self.game.sy]) - self.reference)
        self.ycoord = 0.05*self.reference

        # -----------------------------------------------------------------------------------------
        # THE MAIN GRAPHICS OBJECTS WILL BE STORED
        
        self.laser = Laser(self)

        # -----------------------------------------------------------------------------------------
        # Auxillary utilities
        # -----------------------------------------------------------------------------------------
        
    def buttons(self, ):        
        def hoverclick(pos, h, v):
            click = pg.mouse.get_pressed()
            mx, my = pg.mouse.get_pos()
            if (mx > pos[0] and mx < pos[0]+h) and (my > pos[1] and my < pos[1]+v):
                if click[0] == 1:
                    return True
                
        if self.game.interface.submitted == False:            
            if hoverclick(self.backpos, self.hback, self.vback):
                self.game.mode = "interface"
                time.sleep(3*self.sleep_time)

    def draw_buttons(self, ):
        mx, my = pg.mouse.get_pos()
        def command_button(string, pos, h, v, mx, my, game, font=20):                
            buttonfont = pygame.font.Font('freesansbold.ttf', 18) # font
            if (mx > pos[0] and mx < pos[0]+h) and (my > pos[1] and my < pos[1]+v):
                button = buttonfont.render(string, True, BLUE, None) 
            else:
                button = buttonfont.render(string, True, WHITE, None)

            buttonRect = button.get_rect()
            buttonRect.width = h
            buttonRect.height = v
            buttonRect.center = (pos[0]+0.55*h, pos[1]+0.7*v)
            
            pg.draw.rect(game.display, DBLUE, (pos[0],pos[1], h, v), 1)
            game.display.blit(button, buttonRect)

        if self.game.interface.submitted == False:
            command_button("BACK", self.backpos, self.hback, self.vback, mx, my, self.game)

    def measure(self, ):
        # Allows the player to check coordinates using the mouse when clicking.
        mx, my = pg.mouse.get_pos()
        # position to be displayed
        dx = int(mx/self.game_unit)
        dy = int(my/self.game_unit)
        if pg.mouse.get_pressed()[0] == 1:
            measurefont = pygame.font.Font('freesansbold.ttf', 10)
            measure = measurefont.render(f"{dx}, {dy}", True, WHITE, None)            
            measureRect = measure.get_rect()
            measureRect.center = (mx, my)
            self.game.display.blit(measure, measureRect)
        
    def draw_grid(self, ):
        # dimensions of the grid dependent on the smallest dimension of the game itself.
        # y
        # ------------------------------
        # |        -----------         |
        # |       |           |        |        |
        # |       |     +     |        | smaller distance
        # |       |           |        |        |
        # |        -----------         |
        # ------------------------------x
        
        pg.draw.rect(self.game.display,
                     WHITE,
                     (self.xcoord, self.ycoord, self.reference, self.reference),
                     2)

    def scoring(self,):
        """
        This is used to compare the CURRENT state of the material to the GOAL state.
        The Goal state will have been set in the menu.
        """
        pass

    def info(self,):
        # Displays vital information for the player.
        #  - The state and parameters of the laser
        #  - Their current score
        #  - The score they have to beat
        #  - The amount of energy the laser has left
        pass


    # ------------------------------------------------------------------------------------------
    # LEAD FUNCTIONS
    # ------------------------------------------------------------------------------------------
    
    def UpdateGraphics(self,):
        self.buttons()
        if self.game.interface.submitted == True and self.laser.finished == False:
            self.laser.update_laser()
            
    def DrawGraphics(self,):
        self.game.display.fill(DBLUE)
        self.measure()
        self.draw_grid()
        self.draw_buttons()

        # drawing materials
        self.laser.draw_laser()


