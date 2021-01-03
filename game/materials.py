# Program Name: materials.py
# Author: Aravinthen Rajkumar

import pygame as pg
import numpy as np
import math as m
import time

BLUE = (106, 160, 184)
DBLUE = (0, 0, 128)
LBLUE = (0, 134, 143)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (128, 255, 0)
NEONGREEN = (57, 255, 20)
YELLOW = (255, 255, 0)
SILVER = (192,192,192)
ORANGE = (255, 128, 0)
RED = (255, 0, 0)

def one2two(pos):
    # this is a dreadfully ugly conversion fucntion for the 1d number into the
    # corresponding 2d value
    # used exclusively for the laser position
    # modulo is always 400
    pos = pos%400
    digs = [int(i) for i in str(pos).zfill(3)]
    conv = [digs[0]*100, digs[1]*10 + digs[2]]

    if pos>=300:        
        conv = [0, 100-(pos-300)]
    elif pos>=200:
        conv = [100-(pos-200), 100]
    elif pos>=100:
        conv = [digs[0]*100, digs[1]*10 + digs[2]]
    else:
        conv = [digs[1]*10 + digs[2], 0]    
    return np.array(conv)

def gameconv(pos, ref, unit):
    # convert a position into the relevant game units
    # ref: the point of reference by which everything is defined.
    #      (for this game, everything is measured from top left
    #       corner of this grid).
    conv_pos = np.array([int(ref[0] + pos[0]*unit), int(ref[1] + pos[1]*unit)])

    return conv_pos

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
    def __init__(self, graphics):
        """
        Initialise laser, relevant data (the position, orientation, intensity, state, and 
        energy).
        """
        self.graphics = graphics

        # The position of the laser is ONE DIMENSIONAL with modulo 400 to represent a
        # on a square with unit 100 side length.
        # [0, 100)   --> (0,0), (100, 0)
        # [100, 200) --> (100, 0), (100, 100)
        # [200, 300) --> (100, 100), (0, 100)
        # [300, 400)   --> (0, 100), (0, 0) 
        
        # Note however that the above coordinates aren't what pygame will be reading.
        # In the raw units,
        # [0, 100)   --> (xcoord, ycoord+reference) (xcoord+reference, ycoord+reference)
        # [100, 200) --> (xcoord+reference, ycoord+reference) (xcoord+reference, ycoord)
        # [200, 300) --> (xcoord, ycoord+reference) (xcoord, ycoord)
        # [300, 0)   --> (xcoord, ycoord) (xcoord, ycoord+reference)
        # This will, however, be converted in the "draw laser" method.

        # reference
        self.ref = np.array([self.graphics.xcoord, self.graphics.ycoord])

        # fineness of the laser beam
        # lower fineness == better accuracy, but slower calculation.
        self.fine = 0.1
        
        # State variables
        self.on = True
        self.position = 250
        self.angle = 90
        self.intensity = 0        

        # rotation matrix, dependent on self.angle               
        # drawing
        self.radius = int(m.sqrt(0.3*self.graphics.game.sx))
        
        # default cannon values
        # mag: the distance from the centre of the cannon to the tip
        self.mag = np.array([int(0.005*self.graphics.game.sy), 0])


    def beam_calc(self,):
        """
        This is pretty intensive, so it'll only activate in the main graphics program when
        the beam is on.
        Essentially calculates the end point of the beam. Will be used in both the drawing
        and the materials class.
        """
        # remembering to copy() saves lives

        rot = np.array([[m.cos(m.radians(self.angle)),  m.sin(m.radians(self.angle))],
                        [-m.sin(m.radians(self.angle)),  m.cos(m.radians(self.angle))]])
        position = one2two(self.position) + rot@self.mag
        
        direction = rot@self.mag
        game_pos = gameconv(position, self.ref, self.graphics.game_unit)
        
        xcond = (game_pos[0] > 0) and (game_pos[0]< self.graphics.game.sx)
        ycond = (game_pos[1] > 0) and (game_pos[1]< self.graphics.game.sy)
        while xcond==True and ycond==True:
            # there's no point in initializing a new unit vector each time
            # scaling the fineness will have the required effect

            #-----------------------------------------------------------------------------------
            # TO BE IMPLEMENTED: material collision detection
            #
            #-----------------------------------------------------------------------------------

            position += self.fine*direction
            game_pos = gameconv(position, self.ref, self.graphics.game_unit)
            xcond = (game_pos[0] > 0) and (game_pos[0]< self.graphics.game.sx)
            ycond = (game_pos[1] > 0) and (game_pos[1]< self.graphics.game.sy)

        return position
            
        
    def update_laser(self,):
        """
        Updates the state of the laser variables.
        If the laser's state variable is True, a line will be drawn. 
        """
        self.angle+=1
        self.position+=1
        if (self.angle + self.position) % 48 == 0:
            self.on = not self.on

    def draw_laser(self,):
        """
        NOTE: TRANSFORMATIONS MUST BE APPLIED HERE.
        1. pygame's native coordinate system is (x, -y) for some reason (stupid af). This must
           be accounted for.
        2. The one-dimensional position of the square must be mapped to a two-dimensional
           coordinate system.
        """
        
        pg.draw.circle(self.graphics.game.display,
                       SILVER,
                       gameconv(one2two(self.position), self.ref, self.graphics.game_unit),
                       self.radius)


        # cannon fire:
        rot = np.array([[m.cos(m.radians(self.angle)),  m.sin(m.radians(self.angle))],
                        [-m.sin(m.radians(self.angle)),  m.cos(m.radians(self.angle))]])
        can = one2two(self.position) + rot@self.mag
        
        if self.on == True:
            cancol = GREEN
            start = gameconv(can, self.ref, self.graphics.game_unit)
            end = gameconv(self.beam_calc(), self.ref, self.graphics.game_unit)
            pg.draw.line(self.graphics.game.display, cancol, start, end, 5)
            
        else:
            cancol = ORANGE
            
        pg.draw.circle(self.graphics.game.display,
                       cancol,
                       gameconv(can, self.ref, self.graphics.game_unit),                       
                       int((0.5*(self.intensity/1000) + 0.3)*self.radius))

        
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
            
    NOTE: this needs to be as efficient as possible.
    It's best to build a system that checks the neighbourhood AROUND a point.
    """
        
    def __init__(self, game, laser):
        """
        Initialise material lists and relevant details.
        """
        self.game = game
        
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

