# Program Name: game_file.py
# Description: The complete file for the full hetsys game

import pygame as pg
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

# Colours
BLUE = (106, 160, 184)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class LaserGame:
#-------------------------------------------------------------------------------------------------
#                                        GENERAL USER INTERFACE
# This part of the code is dedicated to the CONTROL of the game: that is, the input.
# It will contain the starting menu, the programming interface and the full laser script language.
# The Laserscript language will be taken as input for the MECHANICS section, which will produce 
# the laser ablation animations.
#-------------------------------------------------------------------------------------------------
    # ------------------------------------------ MENU --------------------------------------------
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

        def Default(self,):
            self.menumode = 'default'
        
        def LevelSelect(self,):
            self.menumode = 'level'

        def HighScores(self,):
            self.menumode = 'highscore'

        def Instructions(self,):
            self.menumode = 'instructions'

        def Credits(self,):
            self.menumode = 'credits'

        def UpdateMenu(self,):
            pass
            
        def DrawMenu(self,):
            # The default menu screen.
            if self.menumode == "default":
                # ------------------------- BACKGROUND -----------------------
                # The Menu background colour is defined over here.
                self.game.display.fill(WHITE)
                
                # ---------------------------- TEXT --------------------------
                # create a text surface object on which text is drawn on it.
                
                # GAME TITLE DEFINED BELOW (obviously subject to change)
                titlefont = pygame.font.Font('freesansbold.ttf', 40) # font
                title = titlefont.render('HETSYS LASER GAME', True, WHITE, BLUE) 
                titleRect = title.get_rect()                              # Initialise the text box
                titleRect.center = (self.game.sx//2, (0.30)*self.game.sy) # rectangle position

                # BUTTONS
                # The PLAY button
                playfont = pygame.font.Font('freesansbold.ttf', 30) # font
                play = playfont.render('PLAY', True, WHITE, BLUE) 
                playRect = title.get_rect()
                playRect.width = 100
                playRect.center = (self.game.sx/2, (0.45)*self.game.sy)

                buttonfont = pygame.font.Font('freesansbold.ttf', 23) # font
                # The instructions button
                instruct = buttonfont.render('Instructions', True, WHITE, BLUE) 
                instructRect = title.get_rect()
                instructRect.width = 100
                instructRect.center = (self.game.sx/2, (0.60)*self.game.sy)

                # The highscores button
                high = buttonfont.render('High Scores', True, WHITE, BLUE) 
                highRect = high.get_rect()
                highRect.width = 100
                highRect.center = (self.game.sx/2, (0.70)*self.game.sy)

                # The credits button
                cred = buttonfont.render('Credits', True, WHITE, BLUE) 
                credRect = cred.get_rect()
                credRect.width = 100
                credRect.center = (self.game.sx/2, (0.80)*self.game.sy)

                # DRAWING IT ALL TO SCREEN -------------------------------------
                self.game.display.blit(title, titleRect)
                self.game.display.blit(instruct, instructRect)
                self.game.display.blit(high, highRect)
                self.game.display.blit(cred, credRect)
                self.game.display.blit(play, playRect)
                
            # The level select screen.
            if self.menumode == "level":
                pass

            # The instructions screen.
            if self.menumode == "instructions":
                pass

            # The 
            if self.menumode == "highscore":
                pass
            if self.menumode == "credits":
                pass
            
    # -------------------------------------  LASER SCRIPT ----------------------------------------
    class LaserScript:
        """
        This is the scripting lanuage that the player will use to control the laser.
        It will be used alongside the interface to generate the input.
        """
        def __init__(self, state, game):
            self.state = state
            self.game = game # this is used to interface with the full game object

    # ---------------------------------------- INTERFACE -----------------------------------------
    class Interface:
        """
        The gameplay is carried out via the interface.
        """
        def __init__(self,state, game):
            self.state = state
            self.game = game # this is used to interface with the full game object

#-------------------------------------------------------------------------------------------------
#                                              MECHANICS
# The animation mechanics are designed around a laser and the material that it interacts with.
# When the laser 
#-------------------------------------------------------------------------------------------------

    # ------------------------------------------ LASER -------------------------------------------
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

        def scoring(self,):
            """
            This is used to compare the CURRENT state of the material to the GOAL state.
            The Goal state will have been set in the menu.
            """
            pass

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
            pass

    def Update(self,):
        """
        Will be used to carry out all updates.
        """
        if self.mode == "menu":
            # All methods relating to updating the menu will be called here.
            self.menu.UpdateMenu()
            self.menu.DrawMenu()
        else:
            pass
        
        pg.display.update()        

    def Input(self,):
        """ 
        Ties in the interface with the laser animations.
        """
        pass
    
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
        pg.display.set_caption("HETSYS - LASER GAME")

        # The objects required to play the game are initialised all together.
        # the second "self" variable is used to access the full LaserGame object from
        # the menu and interface classes.
        # REMEMBER! LOWER CASE: the INITIALISED object
        #           UPPER CASE: the CLASS object
        # In most cases, you should be calling the initialised object.
        self.ls = self.LaserScript("inactive", self)
        self.menu = self.Menu("active", self)
        self.interface = self.Interface("inactive", self)

        self.mode = "menu" # This controls the game mode that the player is currently in.
                           # It is updated on the fly.
                           # Possible modes:  1. menu
                           #                  2. interface
                           
        pg.init() # initialize pygame
        finished = False
        while not finished:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    print("Thank you for playing!")
                    finished = True

            self.Draw()   # fill in the screen
            self.Update() # all of the data updates are wrapped up in this function.

            self.clock.tick(self.framerate) # increases the clock by the number of frames
                                            # specified
        
        pg.quit()

        
#--------------------------------------------------------------------------------------------

# The basic control flow of a game is:

# Initialise the PyGame object.
# While game is running:
#    Draw the current scene.
#    Update variables.
#    Check the new inputs
#     repeat


LaserGame(1200, 800,60)
