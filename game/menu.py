# Program Name: menu.py
# Author: Aravinthen Rajkumar
# Description: Menu code for LaserGame object

import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os
import time

# Colours
BLUE = (106, 160, 184)
LBLUE = (0, 134, 143)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREEN = (128, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)

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

        # sleep_time: used to make space between clicks
        # I admit that this isn't the best solution, as the entire program is halted.
        # However, the use of this mechanism is constrained to the menu and the interface.
        self.sleep_time = 0.085
        
        # button specifications: the size and shape of buttons
        # major: used for large, significant buttons (like Play button)
        # minor: used for basic buttons (like the Credits button)
        self.major_width = 100
        self.major_height = 50
        
        # TO DO: figure out how to accurately position boxes!
        self.minor_width = 100
        self.minor_height = 50
        
        # MENU DATA -------------------------------------------------------------------------------
        # BUTTONS ---------------------------------------------------------------------------------
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

        # LEVEL SELECT DATA -----------------------------------------------------------------------
        # Back button
        self.active_lback = 0
        self.lback_pos = ((0.90)*self.game.sx, (0.50)*self.game.sy)

        # information slide data
        # When mouse hovers over a level button, a description of the level will be displayed
        self.slide_coords = (0.23*self.game.sx,
                             0.01*self.game.sy,
                             0.58*self.game.sx,
                             0.95*self.game.sy)
        
        # level select data
        self.active_lvl1 = 0
        self.lvl1_pos = ((0.10)*self.game.sx, (0.10)*self.game.sy)

        self.active_lvl2 = 0
        self.lvl2_pos = ((0.10)*self.game.sx, (0.30)*self.game.sy)

        self.active_lvl3 = 0
        self.lvl3_pos = ((0.10)*self.game.sx, (0.50)*self.game.sy)

        self.active_lvl4 = 0
        self.lvl4_pos = ((0.10)*self.game.sx, (0.70)*self.game.sy)

        self.active_lvl5 = 0
        self.lvl5_pos = ((0.10)*self.game.sx, (0.90)*self.game.sy)
        
        # INSTRUCTION DATA ------------------------------------------------------------------------
        self.num_pages = 3 # The number of instruction pages.b
                           # Starts at 1, no zero-based numbering
                           # You have to update this variable if you add more pages!
                           
        self.inst_page = 1 # This controls the page display for the instruction slide.
                           # It has to be set to zero whenever instructions are exited
        # BUTTONS ---------------------------------------------------------------------------------                           
        # Next page
        self.active_inext = 0
        self.inext_pos = ((0.90)*self.game.sx, (0.5)*self.game.sy)
        # Previous Page
        self.active_iprev = 0
        self.iprev_pos = ((0.10)*self.game.sx, (0.5)*self.game.sy)
        # Back button.
        self.active_iback = 0
        self.iback_pos = ((0.90)*self.game.sx, (0.90)*self.game.sy)

        # HIGH SCORES DATA ------------------------------------------------------------------------
        # h prefix: the back value reserved for the highscore submode
        # BUTTONS ---------------------------------------------------------------------------------
        # Back button
        self.active_hback = 0
        self.hback_pos = ((0.90)*self.game.sx, (0.90)*self.game.sy)
        
        # CREDIT DATA -----------------------------------------------------------------------------
        # c prefix: the back value reserved for the credits submode
        # BUTTONS ---------------------------------------------------------------------------------
        # Back button
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
                    self.menumode = 'level'
                    time.sleep(self.sleep_time)
                if self.active_inst == 1:                    
                    self.menumode = 'instructions'
                    time.sleep(self.sleep_time)
                if self.active_high == 1:                    
                    self.menumode = 'highscore'
                    time.sleep(self.sleep_time)
                if self.active_cred == 1:                    
                    self.menumode = 'credits'
                    time.sleep(self.sleep_time)
                                
        # --------------------------------------  DEFAULT MENU MODE  --------------------------------------------


        # -------------------------------------     BACK BUTTONS     --------------------------------------------
        if self.menumode == 'level':
            # the back button
            if (
                    ((self.lback_pos[0]-self.minor_width//2 < mx) and (mx < self.lback_pos[0]+self.minor_width//2)) and
                    ((self.lback_pos[1]-self.minor_height//2 < my) and (my < self.lback_pos[1]+self.minor_height//2))
               ):
                self.active_lback = 1                                
            else:
                self.active_lback = 0


            # Level 1
            if (
                    ((self.lvl1_pos[0]-self.minor_width//2 < mx) and (mx < self.lvl1_pos[0]+self.minor_width//2)) and
                    ((self.lvl1_pos[1]-self.minor_height//2 < my) and (my < self.lvl1_pos[1]+self.minor_height//2))
               ):
                self.active_lvl1 = 1                                
            else:
                self.active_lvl1 = 0

            # Level 2
            if (
                    ((self.lvl2_pos[0]-self.minor_width//2 < mx) and (mx < self.lvl2_pos[0]+self.minor_width//2)) and
                    ((self.lvl2_pos[1]-self.minor_height//2 < my) and (my < self.lvl2_pos[1]+self.minor_height//2))
               ):
                self.active_lvl2 = 1                                
            else:
                self.active_lvl2 = 0
            
            # Level 3
            if (
                    ((self.lvl3_pos[0]-self.minor_width//2 < mx) and (mx < self.lvl3_pos[0]+self.minor_width//2)) and
                    ((self.lvl3_pos[1]-self.minor_height//2 < my) and (my < self.lvl3_pos[1]+self.minor_height//2))
               ):
                self.active_lvl3 = 1                                
            else:
                self.active_lvl3 = 0

            # Level 4
            if (
                    ((self.lvl4_pos[0]-self.minor_width//2 < mx) and (mx < self.lvl4_pos[0]+self.minor_width//2)) and
                    ((self.lvl4_pos[1]-self.minor_height//2 < my) and (my < self.lvl4_pos[1]+self.minor_height//2))
               ):
                self.active_lvl4 = 1                                
            else:
                self.active_lvl4 = 0

            if (
                    ((self.lvl5_pos[0]-self.minor_width//2 < mx) and (mx < self.lvl5_pos[0]+self.minor_width//2)) and
                    ((self.lvl5_pos[1]-self.minor_height//2 < my) and (my < self.lvl5_pos[1]+self.minor_height//2))
               ):
                self.active_lvl5 = 1                                
            else:
                self.active_lvl5 = 0                

            if click[0] == 1:
                if self.active_lback == 1:
                    self.menumode = 'default'
                    time.sleep(self.sleep_time)
                    
                if self.active_lvl1 == 1:
                    # A variable must be set to save the user's choice here.
                    print("SQUARE")
                if self.active_lvl2 == 1:
                    print("TBD")
                if self.active_lvl3 == 1:                    
                    print("TBD")
                if self.active_lvl4 == 1:                    
                    print("TBD")
                if self.active_lvl5 == 1:                    
                    print("TBD")
            # -----------------------------------     LEVELS   --------------------------------------------------

        if self.menumode == 'instructions':
            # the back button
            if (
                    ((self.iback_pos[0]-self.minor_width//2 < mx) and (mx < self.iback_pos[0]+self.minor_width//2)) and
                    ((self.iback_pos[1]-self.minor_height//2 < my) and (my < self.iback_pos[1]+self.minor_height//2))
               ):
                self.active_iback = 1                                
            else:
                self.active_iback = 0
                
            # the next page button
            if (
                    ((self.inext_pos[0]-self.minor_width//2 < mx) and (mx < self.inext_pos[0]+self.minor_width//2)) and
                    ((self.inext_pos[1]-self.minor_height//2 < my) and (my < self.inext_pos[1]+self.minor_height//2))
               ):
                self.active_inext = 1                                
            else:
                self.active_inext = 0

            # the previous page button
            if (
                    ((self.iprev_pos[0]-self.minor_width//2 < mx) and (mx < self.iprev_pos[0]+self.minor_width//2)) and
                    ((self.iprev_pos[1]-self.minor_height//2 < my) and (my < self.iprev_pos[1]+self.minor_height//2))
               ):
                self.active_iprev = 1                                
            else:
                self.active_iprev = 0

            # All the available click options:            
            if click[0] == 1:                
                if self.active_iback == 1:
                    self.menumode = 'default'
                    self.inst_page = 1
                    time.sleep(self.sleep_time)
                if self.active_inext == 1 and self.inst_page < self.num_pages:
                    # the inequality makes sure that the next page functionality is disabled
                    # The click pause duration is TWICE as much as the standard.
                    self.inst_page += 1
                    time.sleep(2*self.sleep_time)
                if self.active_iprev == 1 and self.inst_page > 1:
                    self.inst_page -= 1
                    time.sleep(2*self.sleep_time)

                    
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
                    time.sleep(self.sleep_time)

        if self.menumode == 'highscore':
            if (
                    ((self.hback_pos[0]-self.minor_width//2 < mx) and (mx < self.hback_pos[0]+self.minor_width//2)) and
                    ((self.hback_pos[1]-self.minor_height//2 < my) and (my < self.hback_pos[1]+self.minor_height//2))
               ):
                self.active_hback = 1                                
            else:
                self.active_hback = 0

                
            if click[0] == 1:
                if self.active_hback == 1:
                    self.menumode = 'default'
                    time.sleep(self.sleep_time)                    
                
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
            self.game.display.fill(WHITE)
            
            # the BACK button
            lbackfont = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_lback == 1:
                lback = lbackfont.render('BACK', True, WHITE, BLUE)
            else:
                lback = lbackfont.render('BACK', True, WHITE, LBLUE)
                
            lbackRect = lback.get_rect()
            lbackRect.width = self.major_width
            lbackRect.height = self.major_height
            lbackRect.center = self.lback_pos

            # the LEVEL buttons
            # Lvl1
            lvl1font = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_lvl1 == 1:
                lvl1 = lvl1font.render('LEVEL 1', True, WHITE, BLUE)
            else:
                lvl1 = lvl1font.render('LEVEL 1', True, WHITE, LBLUE)                
            lvl1Rect = lvl1.get_rect()
            lvl1Rect.width = self.major_width
            lvl1Rect.height = self.major_height
            lvl1Rect.center = self.lvl1_pos

            # Lvl2
            lvl2font = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_lvl2 == 1:
                lvl2 = lvl2font.render('LEVEL 2', True, WHITE, BLUE)
            else:
                lvl2 = lbackfont.render('LEVEL 2', True, WHITE, LBLUE)                
            lvl2Rect = lvl2.get_rect()
            lvl2Rect.width = self.major_width
            lvl2Rect.height = self.major_height
            lvl2Rect.center = self.lvl2_pos

            # Lvl3
            lvl3font = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_lvl3 == 1:
                lvl3 = lvl3font.render('LEVEL 3', True, WHITE, BLUE)
            else:
                lvl3 = lvl3font.render('LEVEL 3', True, WHITE, LBLUE)                
            lvl3Rect = lvl3.get_rect()
            lvl3Rect.width = self.major_width
            lvl3Rect.height = self.major_height
            lvl3Rect.center = self.lvl3_pos

            # Lvl4
            lvl4font = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_lvl4 == 1:
                lvl4 = lvl4font.render('LEVEL 4', True, WHITE, BLUE)
            else:
                lvl4 = lvl4font.render('LEVEL 4', True, WHITE, LBLUE)                
            lvl4Rect = lvl4.get_rect()
            lvl4Rect.width = self.major_width
            lvl4Rect.height = self.major_height
            lvl4Rect.center = self.lvl4_pos

            # Lvl5
            lvl5font = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_lvl5 == 1:
                lvl5 = lvl5font.render('LEVEL 5', True, WHITE, BLUE)                              
            else:
                lvl5 = lvl5font.render('LEVEL 5', True, WHITE, LBLUE)                
            lvl5Rect = lvl5.get_rect()
            lvl5Rect.width = self.major_width
            lvl5Rect.height = self.major_height
            lvl5Rect.center = self.lvl5_pos
            
            # drawing buttons
            self.game.display.blit(lback, lbackRect)
            self.game.display.blit(lvl1, lvl1Rect)
            self.game.display.blit(lvl2, lvl2Rect)
            self.game.display.blit(lvl3, lvl3Rect)
            self.game.display.blit(lvl4, lvl4Rect)
            self.game.display.blit(lvl5, lvl5Rect)

            # level information slides:
            if self.active_lvl1 == 1:
                pg.draw.rect(self.game.display, BLUE, self.slide_coords)
            if self.active_lvl2 == 1:
                pg.draw.rect(self.game.display, GREEN, self.slide_coords)
            if self.active_lvl3 == 1:
                pg.draw.rect(self.game.display, ORANGE, self.slide_coords)
            if self.active_lvl4 == 1:
                pg.draw.rect(self.game.display, RED, self.slide_coords)
            if self.active_lvl5 == 1:
                pg.draw.rect(self.game.display, BLACK, self.slide_coords)

        # Draw the instructions screen.
        if self.menumode == "instructions":
            # wipe the screen
            self.game.display.fill(WHITE)
            #------------------------------------------------------------------------------------------
            # TUTORIAL TEXT
            # NOTE: If you add a new page, MAKE SURE TO CHANGE THE self.num_pages variable to account for it!
            if self.inst_page == 1:
                pass
            if self.inst_page == 2:
                pass
            if self.inst_page == 3:
                pass
            #------------------------------------------------------------------------------------------
            # BUTTONS            
            # the BACK button
            ibackfont = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_iback == 1:
                iback = ibackfont.render('BACK', True, WHITE, BLUE)
            else:
                iback = ibackfont.render('BACK', True, WHITE, LBLUE)
                
            ibackRect = iback.get_rect()
            ibackRect.width = self.major_width
            ibackRect.height = self.major_height
            ibackRect.center = self.iback_pos

            # the NEXT button
            if self.inst_page < self.num_pages:
                inextfont = pygame.font.Font('freesansbold.ttf', 30) # font
                if self.active_inext == 1:
                    inext = inextfont.render('NEXT', True, WHITE, BLUE)
                else:
                    inext = inextfont.render('NEXT', True, WHITE, LBLUE)
                
                inextRect = inext.get_rect()
                inextRect.width = self.major_width
                inextRect.height = self.major_height
                inextRect.center = self.inext_pos

                # need to draw this separately, as it's dependent on self.inst_page 
                self.game.display.blit(inext, inextRect)            

            # the PREV button
            if self.inst_page > 1:
                iprevfont = pygame.font.Font('freesansbold.ttf', 30) # font                
                if self.active_iprev == 1:
                    iprev = iprevfont.render('PREVIOUS', True, WHITE, BLUE)
                else:
                    iprev = iprevfont.render('PREVIOUS', True, WHITE, LBLUE)
                
                iprevRect = iprev.get_rect()
                iprevRect.width = self.major_width
                iprevRect.height = self.major_height
                iprevRect.center = self.iprev_pos
                
                # need to draw this separately, as it's dependent on self.inst_page    
                self.game.display.blit(iprev, iprevRect) 
                
            # Drawing
            self.game.display.blit(iback, ibackRect)
        
        # Draw the highscore screen
        if self.menumode == "highscore":
            # wipe the screen
            self.game.display.fill(WHITE)
            # BUTTONS
            # the BACK button
            hbackfont = pygame.font.Font('freesansbold.ttf', 30) # font
            if self.active_hback == 1:
                hback = hbackfont.render('BACK', True, WHITE, BLUE)
            else:
                hback = hbackfont.render('BACK', True, WHITE, LBLUE)
                
            hbackRect = hback.get_rect()
            hbackRect.width = self.major_width
            hbackRect.height = self.major_height
            hbackRect.center = self.hback_pos

            self.game.display.blit(hback, hbackRect)

        # Draw the credits screen
        if self.menumode == "credits":
            # wipe the screen
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
