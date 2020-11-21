# Program Name: menu.py
# Author: Aravinthen Rajkumar
# Description: Menu code for LaserGame object

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

class Menu:
    """
    This will be used as a loop point. When the player finishes playing, the program will 
    automatically return here.
    The menu will contain an option for starting a new game, exiting the game or seeing the
    high scores.
    The STARTING SHAPE and GOAL SHAPE will be determined here.
    """
    def __init__(self, state, game):
        # state can be "active" or "inactive" depending on use.
        self.state = state
        self.game = game          # this is used to interface with the full game object
        
        self.menumode = "default" # These are the submodes associated with the menu object.
        # There are four, corresponding to the different forms
        # available within the menu screen.
        # Options: a) default
        #          b) level:        the level selection screen
        #          c) highscore:    the highscores screen
        #          d) instructions: 
        #          e) credits:      the credits screen


        # button specifications: the size and shape of buttons
        # major: used for large, significant buttons (like Play button)
        # minor: used for basic buttons (like the Credits button)
        self.major_width = 100
        self.major_height = 50
        
        # TO DO: figure out how to accurately position boxes!
        self.minor_width = 100
        self.minor_height = 50
        
        # MENU BUTTONS----------------------------------------------------------------------------
        # active_{button}: whether the button is active or not
        # {button}_pos:    the position of the button
        #                  these are all located in the __init__ object to ensure that any
        #                  changes will be global.
        self.active_play = 0
        self.play_pos = (self.game.sx/2, (0.45)*self.game.sy)
        # instructions
        self.active_inst = 0
        self.inst_pos = (self.game.sx/2, (0.60)*self.game.sy)
        # highscores
        self.active_high = 0
        self.high_pos = (self.game.sx/2, (0.70)*self.game.sy)
        # credits
        self.active_cred = 0
        self.cred_pos = (self.game.sx/2, (0.80)*self.game.sy)
        
        # INSTRUCTION BUTTONS---------------------------------------------------------------------

        # HIGH SCORES BUTTONS---------------------------------------------------------------------
        
        # CREDIT BUTTONS--------------------------------------------------------------------------
        # c prefix: the back value reserved for the credits submode
        self.active_cback = 0
        self.cback_pos = ((0.90)*self.game.sx, (0.90)*self.game.sy)
        
    def UpdateMenu(self,):
        mx, my = pg.mouse.get_pos() # mouse coordinates
        click = pg.mouse.get_pressed() # click[0]: left click
        
        # --------------------------------------  DEFAULT MENU MODE  --------------------------------------------
        if self.menumode == "default":
            # -------------------------------------- BUTTON INTERACTIVITY -----------------------------------------
            # This section controls the interactivity of the buttons.
            # NOTE: if you want to move a button, you have to change the values in the initial object!
            # the play button
            if (
                    ((self.play_pos[0]-self.minor_width//2 < mx) and (mx < self.play_pos[0]+self.minor_width//2)) and
                    ((self.play_pos[1]-self.minor_height//2 < my) and (my < self.play_pos[1]+self.minor_height//2))
               ):
                self.active_play = 1                                
            else:
                self.active_play = 0

            # the instructions button 
            if (
                    ((self.inst_pos[0]-self.minor_width//2 < mx) and (mx < self.inst_pos[0]+self.minor_width//2)) and
                    ((self.inst_pos[1]-self.minor_height//2 < my) and (my < self.inst_pos[1]+self.minor_height//2))
               ):
                self.active_inst = 1
            else:
                self.active_inst = 0
            
            # the high scores button 
            if (
                    ((self.high_pos[0]-self.minor_width//2 < mx) and (mx < self.high_pos[0]+self.minor_width//2)) and
                    ((self.high_pos[1]-self.minor_height//2 < my) and (my < self.high_pos[1]+self.minor_height//2))
               ):
                self.active_high = 1
            else:
                self.active_high = 0            

            # the credits button 
            if (
                    ((self.cred_pos[0]-self.minor_width//2 < mx) and (mx < self.cred_pos[0]+self.minor_width//2)) and
                    ((self.cred_pos[1]-self.minor_height//2 < my) and (my < self.cred_pos[1]+self.minor_height//2))
               ):
                self.active_cred = 1
            else:
                self.active_cred = 0

            # -------------------------------------- BUTTON CLICK DETECTION  --------------------------------------
            # Used to detect clicking
            # switching from one submode to another
            if click[0] == 1:
                if self.active_play == 1:                    
                    print("NOT YET IMPLEMENTED!")
                if self.active_inst == 1:                    
                    print("NOT YET IMPLEMENTED!")
                if self.active_high == 1:                    
                    print("NOT YET IMPLEMENTED!")            
                if self.active_cred == 1:                    
                    self.menumode = 'credits'
                    
        # --------------------------------------  DEFAULT MENU MODE  --------------------------------------------
        if self.menumode == 'credits':
            if (
                    ((self.cback_pos[0]-self.minor_width//2 < mx) and (mx < self.cback_pos[0]+self.minor_width//2)) and
                    ((self.cback_pos[1]-self.minor_height//2 < my) and (my < self.cback_pos[1]+self.minor_height//2))
               ):
                self.active_cback = 1                                
            else:
                self.active_cback = 0

                
            if click[0] == 1:
                if self.active_cback == 1:
                    self.menumode = 'default'
                    
                
    def DrawMenu(self,):
        # The default menu screen.
        if self.menumode == "default":
            # ------------------------- BACKGROUND -----------------------
            # The Menu background colour is defined over here.
            self.game.display.fill(WHITE)
            # ---------------------------- TEXT --------------------------
            # create a text surface object on which text is drawn on it.
            
            # GAME TITLE DEFINED BELOW (obviously subject to change)
            titlefont = pygame.font.Font('freesansbold.ttf', 50) # font
            title = titlefont.render('laser.io', True, BLUE, WHITE) 
            titleRect = title.get_rect()                              # Initialise the text box
            titleRect.center = (self.game.sx//2, (0.30)*self.game.sy) # rectangle position

            # BUTTONS
            # The PLAY button
            playfont = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_play == 1:
                play = playfont.render('PLAY', True, WHITE, BLUE)
            else:
                play = playfont.render('PLAY', True, WHITE, LBLUE)
            playRect = title.get_rect()
            playRect.width = self.major_width
            playRect.height = self.major_height
            playRect.center = self.play_pos
            
            buttonfont = pygame.font.Font('freesansbold.ttf', 23) # font for buttons
            
            # The instructions button
            if self.active_inst == 1:
                instruct = buttonfont.render('Instructions', True, WHITE, BLUE)
            else:
                instruct = buttonfont.render('Instructions', True, WHITE, LBLUE)
            instructRect = title.get_rect()
            instructRect.width = self.minor_width
            instructRect.height = self.minor_height
            instructRect.center = self.inst_pos
            
            # The highscores button
            if self.active_high == 1:
                high = buttonfont.render('High Scores', True, WHITE, BLUE)
            else:
                high = buttonfont.render('High Scores', True, WHITE, LBLUE)                
            highRect = high.get_rect()
            highRect.width = self.minor_width
            highRect.height = self.minor_height
            highRect.center = self.high_pos
            
            # The credits button
            if self.active_cred == 1:
                cred = buttonfont.render('Credits', True, WHITE, BLUE)
            else:
                cred = buttonfont.render('Credits', True, WHITE, LBLUE)                
            credRect = cred.get_rect()
            credRect.width = self.minor_width
            credRect.height = self.minor_height
            credRect.center = self.cred_pos
            
            # DRAWING IT ALL TO SCREEN -------------------------------------
            self.game.display.blit(title, titleRect)
            self.game.display.blit(instruct, instructRect)
            self.game.display.blit(high, highRect)
            self.game.display.blit(cred, credRect)
            self.game.display.blit(play, playRect)
            
        # Draw the level select screen.
        if self.menumode == "level":
            pass

        # Draw the instructions screen.
        if self.menumode == "instructions":
            pass
        
        # Draw the highscore screen
        if self.menumode == "highscore":
            pass

        # Draw the credits screen
        if self.menumode == "credits":
            self.game.display.fill(WHITE)

            # CREDITS
            titlefont = pygame.font.Font('freesansbold.ttf', 30) # font
            title = titlefont.render('CREDITS', True, BLACK, WHITE)
            titleRect = title.get_rect()
            titleRect.width = 100
            titleRect.height = 30
            titleRect.center = ((0.2)*self.game.sx, (0.10)*self.game.sy)

            # CREDITS
            progfont = pygame.font.Font('freesansbold.ttf', 19) # font
            prog = progfont.render('Programming', True, BLACK, WHITE)
            progRect = prog.get_rect()
            progRect.width = 50
            progRect.height = 30
            progRect.center = ((0.20)*self.game.sx, (0.20)*self.game.sy)
            
            arrefont = pygame.font.Font('freesansbold.ttf', 19) # font
            arre = arrefont.render('Aravinthen Rajkumar', True, BLACK, WHITE)
            arreRect = arre.get_rect()
            arreRect.width = 50
            arreRect.height = 30
            arreRect.center = (self.game.sx/2, (0.20)*self.game.sy)
            
            # BUTTONS
            # the BACK button
            cbackfont = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_cback == 1:
                cback = cbackfont.render('BACK', True, WHITE, BLUE)
            else:
                cback = cbackfont.render('BACK', True, WHITE, LBLUE)
                
            cbackRect = cback.get_rect()
            cbackRect.width = self.major_width
            cbackRect.height = self.major_height
            cbackRect.center = self.cback_pos

            self.game.display.blit(title, titleRect)
            self.game.display.blit(prog, progRect)
            self.game.display.blit(arre, arreRect)
            self.game.display.blit(cback, cbackRect)
