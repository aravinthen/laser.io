# Program Name: materials.py
# Author: Aravinthen Rajkumar

import pygame as pg
import random
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


#---------------------------------------------------------------------------------------------
# LEVELS
# Relocate this block of code!
# Key:    1 - material blocks to be removed.
#         2 - forbidden blocks, removing these reduces score.

level1 = np.array([[0,0,0,0,0,0],
                   [0,1,1,1,1,0],
                   [0,1,2,2,1,0],
                   [0,1,2,2,1,0],
                   [0,1,1,1,1,0],
                   [0,0,0,0,0,0]])

level2 = np.array([[0,0,0,0,0,0,0,0,0,0],
                   [0,1,1,1,1,1,1,1,1,0],
                   [0,1,1,1,2,2,1,1,1,0],
                   [0,1,1,2,2,2,2,1,1,0],
                   [0,1,2,2,2,2,2,2,1,0],
                   [0,1,2,2,2,2,2,2,1,0],
                   [0,1,1,2,2,2,2,1,1,0],
                   [0,1,1,1,1,1,1,1,1,0],
                   [0,0,1,1,1,1,1,1,0,0],
                   [0,0,0,0,0,0,0,0,0,0]])

level3 = np.array([[0,0,0,0,0,0],
                   [0,1,1,1,1,0],
                   [0,1,2,2,1,0],
                   [0,1,1,2,1,0],
                   [0,1,1,1,1,0],
                   [0,0,0,0,0,0]])

level4 = np.array([[0,0,0,0,0,0],
                   [0,1,1,1,1,0],
                   [0,1,2,1,1,0],
                   [0,1,2,2,1,0],
                   [0,1,1,1,1,0],
                   [0,0,0,0,0,0]])

level5 = np.array([[0,0,0,0,0,0],
                   [0,1,1,1,1,0],
                   [0,1,1,2,1,0],
                   [0,1,2,1,1,0],
                   [0,1,1,1,1,0],
                   [0,0,0,0,0,0]])


# add all level variables to the list in order, will allow easy calling 
level_list = [level1, level2, level3, level4, level5]

#---------------------------------------------------------------------------------------------

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
        self.game = self.graphics.game
        self.interface = self.graphics.game.interface

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
        self.read_commands = None
        self.finished = False

        # fineness of the laser beam
        # lower fineness == better accuracy, but slower calculation.
        self.fine = 0.1
        
        # State variables
        self.on = False
        self.error = False
        self.position = 250
        self.angle = 90
        self.intensity = 2

        # rotation matrix, dependent on self.angle               
        # drawing
        self.radius = int(m.sqrt(0.3*self.graphics.game.sx))
        
        # default cannon values
        # mag: the distance from the centre of the cannon to the tip
        self.mag = np.array([int(0.005*self.graphics.game.sy), 0])

    def reset(self,):
        self.on = False
        self.error = False
        self.position = 250
        self.angle = 90
        self.intensity = 2

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

            # material collision detection
            position += self.fine*direction
            game_pos = gameconv(position, self.ref, self.graphics.game_unit)

            # conditions for gamepos[0]
            lx0 = (game_pos[0] > self.graphics.materials.graph_x)
            lx1 = (game_pos[0] < self.graphics.materials.graph_x + self.graphics.materials.graph_h)
            
            # conditions for gamepos[1]
            ly0 = (game_pos[1] > self.graphics.materials.graph_y)
            ly1 = (game_pos[1] < self.graphics.materials.graph_y + self.graphics.materials.graph_v)

            if lx0 and lx1 and ly0 and ly1:
                index1 = int(game_pos[0] - self.graphics.materials.graph_x)
                index2 = int(game_pos[1] - self.graphics.materials.graph_y)
                
                collision = self.graphics.materials.matpix[index1, index2][2] != 128
                
                if collision.all():
                    for i in range(-self.intensity,self.intensity):
                        for j in range(-self.intensity,self.intensity):
                            self.graphics.materials.matpix[index1+i, index2+j] = np.array(DBLUE)
                    break
            
            xcond = (game_pos[0] > 0) and (game_pos[0]< self.graphics.game.sx)
            ycond = (game_pos[1] > 0) and (game_pos[1]< self.graphics.game.sy)

        return position
            
        
    def update_laser(self,):
        """
        Updates the state of the laser variables.
        If the laser's state variable is True, a line will be drawn. 
        """
        if self.interface.index == len(self.interface.program):
            self.finished = True
            return 0
        
        current_command = self.interface.program[self.interface.index].split(" ")
        argument = current_command[0]
        value = int(current_command[1])

        # for numerical arguments,
        #  1. reduce the argument in the list by one
        #  2. increment the corresponding state variable of the laser by one.
        #  3. if zero, increment the index of the list.
        
        if value == 0:
            self.interface.index += 1
        else:
            # Remember: FOR doesn't turn up here.
            #           it's dealt with in the "parsing" function and performed automatically.
            if argument == "TON":
                self.interface.program[self.interface.index] = "TON " + str(value-1)
                self.on = True
                
            if argument == "TOF":
                self.interface.program[self.interface.index] = "TOF " + str(value-1)
                self.on = False
                
            if argument == "PAU":
                self.interface.program[self.interface.index] = "PAU " + str(value-1)

            if argument == "INT":
                self.intensity = value
                self.interface.index+=1
                
            if argument == "MOV":
                self.interface.program[self.interface.index] = "MOV " + str(value-np.sign(value))
                self.position += np.sign(value)

            if argument == "ORI":
                self.interface.program[self.interface.index] = "ORI " + str(value-np.sign(value))
                self.angle += np.sign(value)
        
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
            pg.draw.line(self.graphics.game.display, cancol, start, end, (int(self.intensity/10)+1))
            
        else:
            cancol = ORANGE
            
        pg.draw.circle(self.graphics.game.display,
                       cancol,
                       gameconv(can, self.ref, self.graphics.game_unit),                       
                       int((0.5*(self.intensity/100) + 0.3)*self.radius))

        
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
    #-----------------------------------------------------------------------------------------------
    
    def __init__(self, graphics, laser):
        """ 
        Initialise material lists and relevant details.
        """
        self.graphics = graphics
        self.laser = laser

        # dimensions of the box
        self.graph_h = int(0.91*self.graphics.reference)+1
        self.graph_v = int(0.91*self.graphics.reference)+1

        # coordinates of the origin of the material matrix        
        self.graph_x = self.graphics.xcoord + 0.03*self.graphics.game.sx
        self.graph_y = self.graphics.ycoord + 0.04*self.graphics.game.sy

        self.level = None
        # the level matrix, designed by hand
        self.level_matrix = None # initially none, but updated once the level is selected.


    def init_level(self, level, bgcol=DBLUE):
        self.level = level
        self.level_matrix = level_list[level-1]                
        # build the pixel version of the level matrix
        n = np.shape(self.level_matrix)[0]
        
        
        blockx = int(self.graph_h/n)
        blocky = int(self.graph_v/n)

        
        self.matpix = np.zeros((self.graph_h, self.graph_v, 3), dtype=np.uint8)
        self.matpix[:, :, 0] = bgcol[0]
        self.matpix[:, :, 1] = bgcol[1]
        self.matpix[:, :, 2] = bgcol[2]
        
        for i in range(0,n):
            for j in range(0,n):
                iind = i*blockx
                jind = j*blocky
                if self.level_matrix[i,j] == 2:
                    for graphi in range(0, blockx):
                        for graphj in range(0, blocky):
                            self.matpix[iind+graphi, jind+graphj, 0] = RED[0] - random.randrange(50)
                            self.matpix[iind+graphi, jind+graphj, 1] = RED[1]
                            self.matpix[iind+graphi, jind+graphj, 2] = RED[2]
                if self.level_matrix[i,j] == 1:
                    for graphi in range(0, blockx):
                        for graphj in range(0, blocky):
                            self.matpix[iind+graphi, jind+graphj, 0] = ORANGE[0] - random.randrange(50)
                            self.matpix[iind+graphi, jind+graphj, 1] = ORANGE[1]
                            self.matpix[iind+graphi, jind+graphj, 2] = ORANGE[2]
                    
    def draw_material(self):
        """
        Draws the materials.
        """
        drawn_matpix = pg.surfarray.make_surface(self.matpix)        
        self.graphics.game.display.blit(drawn_matpix, (self.graph_x, self.graph_y))

