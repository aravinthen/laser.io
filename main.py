# Program Name: game_file.py
# Description: The complete file for the full hetsys game

import pygame as pg
import math as m
import os

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
        def __init__(self,):
            pass
    
    # -------------------------------------  LASER SCRIPT ----------------------------------------
    class LaserScript:
        """
        This is the scripting lanuage that the player will use to control the laser.
        It will be used alongside the interface to generate the input.
        """
        def __init__(self,):
            pass

    # ---------------------------------------- INTERFACE -----------------------------------------
    class Interface:
        """
        The gameplay is carried out via the interface.
        """
        def __init__(self,):
            pass

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
    def __init__(self,):
        """
        Here is where the full game is initialized.
        Everything to do with the actual running of the game goes in here: Pygame, game metadata,
        and the parameters needed to make different parts of the game interact with eachother.
        """
        pass                    

    def draw(self,):
        """
        Takes everything from the above and draws it onto the relevant screen.
        """
        pass

    def update(self,):
        """
        Will be used to carry out all updates.
        """

    def input(self,):
        """ 
        Ties in the interface with the laser animations.
        """
        pass
    
    # --------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------

# The basic control flow of a game is:

# Initialise the PyGame object.
# While game is running:
#    Draw the current scene.
#    Update variables.
#    Check the new inputs
#     repeat


    
    


