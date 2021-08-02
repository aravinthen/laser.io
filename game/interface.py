# Program Name: interface.py
# Author: Aravinthen Rajkumar

import pygame as pg
import pygame.freetype
import time
from pygame.sprite import Sprite
from pygame.rect import Rect
import math as m
import os

# Colours
BLUE = (106, 160, 184)
LBLUE = (0, 134, 143)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (128, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
NEONGREEN = (57, 255, 20)
RED = (255, 0, 0)

class Interface:
    """
    The gameplay is carried out via the interface.
    """    
    def __init__(self, game):
        self.game = game # this is used to interface with the full game object
        # NUM ENTRY FLAG:
        # this activates the calculator mode used to input numbers
        # It must be called with respect to the command.
        self.num_entry = False
        self.valid_entry = False # only true when enter key is pressed
        self.num = ""

        # program details
        self.submitted = False # if the program has been submitted, this will be set as true.
        self.index = 0 # the index that the program is currently on.
        self.program_error = False
        self.program = []
        self.high_level = [] # used for the display

        # sleep time between button clicks
        self.sleep_time = 0.05
        
        # BUTTONS -----------------------------------------------------------------------------------
        #  Button details are located within the object itself. This ensures that they can
        #  be used between methods as well as gathered in one section for easier access.
                       
        # -------------------------------- CALCULATOR -------------------------------------
        # calculator position
        self.cx = 0.52*self.game.sx
        self.cy = 0.1*self.game.sy

        # enter
        self.entpos = (1.1*self.cx, 2.5*self.cy)
        self.enth = 0.1*self.game.sx
        self.entv = 0.05*self.game.sy

        # delete
        self.delpos = (1.1*self.cx, 3.5*self.cy)    
        self.delh = 0.1*self.game.sx
        self.delv = 0.05*self.game.sy

        # cancel
        self.canpos =(1.1*self.cx, 4.5*self.cy)
        self.canh = 0.1*self.game.sx
        self.canv = 0.05*self.game.sy

        # numbers
        self.pos0 =(1.4*self.cx, 4.5*self.cy)
        self.h0 = 0.04*self.game.sx
        self.v0 = 0.05*self.game.sy
        
        self.pos1 =(1.5*self.cx, 4.5*self.cy)
        self.h1 = 0.04*self.game.sx
        self.v1 = 0.05*self.game.sy
        
        self.pos2 =(1.6*self.cx, 4.5*self.cy)
        self.h2 = 0.04*self.game.sx
        self.v2 = 0.05*self.game.sy
        
        self.pos3 =(1.7*self.cx, 4.5*self.cy)
        self.h3 = 0.04*self.game.sx
        self.v3 = 0.05*self.game.sy
        
        self.pos4 =(1.4*self.cx, 3.5*self.cy)
        self.h4 = 0.04*self.game.sx
        self.v4 = 0.05*self.game.sy
        
        self.pos5 =(1.5*self.cx, 3.5*self.cy)
        self.h5 = 0.04*self.game.sx
        self.v5 = 0.05*self.game.sy
        
        self.pos6 =(1.6*self.cx, 3.5*self.cy)
        self.h6 = 0.04*self.game.sx
        self.v6 = 0.05*self.game.sy
        
        self.pos7 =(1.7*self.cx, 3.5*self.cy)
        self.h7 = 0.04*self.game.sx
        self.v7 = 0.05*self.game.sy
        
        self.pos8 =(1.4*self.cx, 2.5*self.cy)
        self.h8 = 0.04*self.game.sx
        self.v8 = 0.05*self.game.sy
        
        self.pos9 =(1.5*self.cx, 2.5*self.cy)
        self.h9 = 0.04*self.game.sx
        self.v9 = 0.05*self.game.sy
        
        self.posd = (1.6*self.cx, 2.5*self.cy)
        self.hd = 0.04*self.game.sx
        self.vd = 0.05*self.game.sy
        
        self.posm =(1.7*self.cx, 2.5*self.cy)
        self.hm = 0.04*self.game.sx
        self.vm = 0.05*self.game.sy

        # -------------------------------- FUNCTIONS ------------------------------------------------
        # These functions implement the main commands of the game.
        #------------------------------------------------------------------------------------
        # FUNCTION        | Symbol | Calculator | Description
        #------------------------------------------------------------------------------------
        # TURN ON:        | TON    | N          | Sets the ON command
        # TURN OFF:       | TOF    | N          | Sets the OFF command
        # PAUSE:          | PAU    | Y          | Pauses program
        # SET INTENSITY:  | INT    | Y          | Sets intensity of the laser.
        # MOVE:           | MOV    | Y          | Moves the the laser along the grid.
        # ORIENT:         | ORI    | Y          | Turns the laser about it's own midpoint.
        # START FOR LOOP: | SFR    | Y          | Set a for loop.
        # END FOR LOOP:   | EFR    | N          | Close a for loop.
        
        # turn on
        self.tonpos = (0.55*self.game.sx, 0.6*self.game.sy)
        self.hton = 0.125*self.game.sx
        self.vton = 0.05*self.game.sy

        # turn off
        self.tofpos = (0.7*self.game.sx, 0.6*self.game.sy)
        self.htof = 0.125*self.game.sx
        self.vtof = 0.05*self.game.sy

        # pause
        self.paupos = (0.55*self.game.sx, 0.7*self.game.sy)
        self.hpau = 0.125*self.game.sx
        self.vpau = 0.05*self.game.sy

        # intensity
        self.intpos = (0.7*self.game.sx, 0.7*self.game.sy)
        self.hint = 0.125*self.game.sx
        self.vint = 0.05*self.game.sy

        # MOVE
        self.movpos = (0.55*self.game.sx, 0.8*self.game.sy)
        self.hmov = 0.125*self.game.sx
        self.vmov = 0.05*self.game.sy

        # orientation
        self.oripos = (0.7*self.game.sx, 0.8*self.game.sy)
        self.hori = 0.125*self.game.sx
        self.vori = 0.05*self.game.sy

        # FOR LOOP
        self.foron = 0 # if a for loop is called, this will be set as 1
        # start/end for loop (both buttons on the same position, called conditionally based on
        #                     self.foron)
        self.forpos = (0.55*self.game.sx, 0.9*self.game.sy)
        self.hfor = 0.125*self.game.sx
        self.vfor = 0.05*self.game.sy

        # delete line
        self.backpos = (0.7*self.game.sx, 0.9*self.game.sy)
        self.hback = 0.125*self.game.sx
        self.vback = 0.05*self.game.sy

        #-----------------------------------------------------------------------------------------
        # OTHER FUNCTIONs
        # - Switching to graphics.
        # - Submitting program.
        # - back to menu.
        #-----------------------------------------------------------------------------------------
        # switch to graphics.
        self.graphpos = (0.85*self.game.sx, 0.6*self.game.sy)
        self.hgraph = 0.125*self.game.sx
        self.vgraph = 0.05*self.game.sy

        # submit
        self.subpos = (0.85*self.game.sx, 0.70*self.game.sy)
        self.hsub = 0.125*self.game.sx
        self.vsub = 0.25*self.game.sy

        # quit
        self.quitpos = (0.90*self.game.sx, 0.01*self.game.sy)
        self.hquit = 0.08*self.game.sx
        self.vquit = 0.05*self.game.sy        


    def reset(self,):
        # resets everything to default
        self.submitted = False # if the program has been submitted, this will be set as true.
        self.index = 0 # the index that the program is currently on.
        self.program_error = False
        self.program = []
        self.high_level = [] # used for the display
        
    # --------------------------------------------------------------------------------------------
    # Parsing
    # Used in "command input"
    # --------------------------------------------------------------------------------------------
    def parse(self,):
        for line in range(len(self.program)):
            current_command = self.program[line].split(" ")
            if (current_command[0] in ["PAU", "INT", "FOR"]) and (int(current_command[1]) < 0):
                return False, line

            if current_command[0] == "SFR":
                loops = line # beginning of loop
                
                loop_count = line # will be assigned to loopf when completed.
                closed = False
                while loop_count < len(self.program):
                    if self.program[loop_count].split(" ")[0] == "EFR":
                        closed = True
                        loopf = loop_count
                        break
                    else:
                        loop_count+=1
                        
                if closed == False:
                    return False, line
                else:
                    # cut the list into the beginning,
                    start_list = self.program[0:loops]
                    # the end,
                    end_list = self.program[loopf+1:]
                    # and the middle part that has to be repeated.
                    loop_list = self.program[loops+1:loopf]

                    self.program = start_list + int(current_command[1])*loop_list + end_list
                    
                    # repeats the procedure until no SFRs or EFRs exist in the program string.
                    # this is so lazy, i fucking love it
                    self.parse()
        else:
            return True, -1
    
    # --------------------------------------------------------------------------------------------
    # COMMAND FUNCTIONS
    # --------------------------------------------------------------------------------------------
    def command_input(self, ):        
        def hoverclick(pos, h, v):
            click = pg.mouse.get_pressed()
            mx, my = pg.mouse.get_pos()
            if (mx > pos[0] and mx < pos[0]+h) and (my > pos[1] and my < pos[1]+v):
                if click[0] == 1:
                    return True

        # Turn on 
        if hoverclick(self.tonpos, self.hton, self.vton):
            self.program.append("TON 1")
            if self.foron == 1:
                self.high_level.append("> LASER.STATUS = ON")
            else:
                self.high_level.append("LASER.STATUS = ON")
            time.sleep(3*self.sleep_time)

            
        # Turn off
        if hoverclick(self.tofpos, self.htof, self.vtof):
            self.program.append("TOF 1")
            if self.foron == 1:
                self.high_level.append(">  LASER.STATUS = OFF")
            else:
                self.high_level.append("LASER.STATUS = OFF")
            time.sleep(3*self.sleep_time)


        # Pause
        if hoverclick(self.paupos, self.hpau, self.vpau):
            self.num_entry = True
            self.program.append("PAU ")
            if self.foron == 1:
                self.high_level.append("> LASER.COMMAND(PAUSE) = [SEC] ")
            else:
                self.high_level.append("LASER.COMMAND(PAUSE) = [SEC] ")
            time.sleep(3*self.sleep_time)

        # Intensity
        if hoverclick(self.intpos, self.hint, self.vint):
            self.num_entry = True
            self.program.append("INT ")
            if self.foron == 1:
                self.high_level.append("> LASER.COMMAND(INTENSITY) = [TW] ")
            else:
                self.high_level.append("LASER.COMMAND(INTENSITY) = [TW] ")
            time.sleep(3*self.sleep_time)

        # Movement
        if hoverclick(self.movpos, self.hmov, self.vmov):
            self.num_entry = True
            self.program.append("MOV ")
            if self.foron == 1:
                self.high_level.append("> LASER.COMMAND(MOVE) = [MM] ")
            else:
                self.high_level.append("LASER.COMMAND(MOVE) = [MM] ")
            time.sleep(3*self.sleep_time)

        # orient
        if hoverclick(self.oripos, self.hori, self.vori):
            self.num_entry = True
            self.program.append("ORI ")
            if self.foron == 1:
                self.high_level.append("> LASER.COMMAND(ORIENTATION) = [DEG] ")
            else:
                self.high_level.append("LASER.COMMAND(ORIENTATION) = [DEG] ")
            time.sleep(3*self.sleep_time)

        # for loop start
        if self.foron == 0:
            if hoverclick(self.forpos, self.hfor, self.vfor):
                self.foron = 1
                self.num_entry = True
                self.program.append("SFR ")
                self.high_level.append("FOR ITERATION IN RANGE ")
                time.sleep(3*self.sleep_time)
        else:
            # for loop end
            if hoverclick(self.forpos, self.hfor, self.vfor):
                self.program.append("EFR")
                self.foron = 0
                time.sleep(3*self.sleep_time)

        # delete line
        if hoverclick(self.backpos, self.hback, self.vback):
            if self.foron == 1 and self.program[len(self.program)-1].split(" ")[0] == "SFR":
                self.foron = 0

            self.program = self.program[0:len(self.program)-1]
            self.high_level = self.high_level[0:len(self.high_level)-1]
            time.sleep(3*self.sleep_time)
            
        # switch to graphics
        if hoverclick(self.graphpos, self.hgraph, self.vgraph):
            self.game.mode = "graphics"
            time.sleep(0.5*self.sleep_time)

        # quit
        if hoverclick(self.quitpos, self.hquit, self.vquit):
            self.game.mode = "menu"
            self.game.level = None
            self.program = []
            self.high_level = []
            time.sleep(3*self.sleep_time)
            
        # submit code
        if hoverclick(self.subpos, self.hsub, self.vsub):
            # ----------------------------------------------------------------------------
            # FULL PARSING
            # This is where the submitted code is checked and for-loops are expanded.
            success, error_line = self.parse()
            if success:
                self.game.mode = "graphics"
                self.submitted = True
            else:
                self.program_error = 1
                self.program.append("ERR 1")
                self.high_level.append("ERROR ON LINE " + str(error_line+1))
                print("ERROR")
            # ----------------------------------------------------------------------------
            time.sleep(3*self.sleep_time)
    
    def number_input(self,):
        # allows the user to input numbers for commands that need them
        click = pg.mouse.get_pressed()
        
        def hoverclick(pos, h, v):
            mx, my = pg.mouse.get_pos()
            if (mx > pos[0] and mx < pos[0]+h) and (my > pos[1] and my < pos[1]+v):
                if click[0] == 1:
                    return True

        if (hoverclick(self.entpos, self.enth, self.entv) == True):
            self.program[-1] += f"{self.num}"
            self.high_level[-1] += f"{self.num}"
            self.num = ""
            
                
            self.num_entry = False

        if hoverclick(self.canpos, self.canh, self.canv) == True:
            self.num = ""            
            self.program = self.program[0:len(self.program)-1]
            self.high_level = self.high_level[0:len(self.high_level)-1]
            self.num_entry = False
            time.sleep(self.sleep_time)
            
        if (hoverclick(self.delpos, self.delh, self.delv) == True) and (len(self.num) != 0):
            self.num = self.num[0:len(self.num)-1]            
            time.sleep(3*self.sleep_time)
            
        if hoverclick(self.pos0, self.h0, self.v0) == True:
            self.num += "0"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos1, self.h1, self.v1) == True:
            self.num += "1"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos2, self.h2, self.v2) == True:
            self.num += "2"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos3, self.h3, self.v3) == True:
            self.num += "3"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos4, self.h4, self.v4) == True:
            self.num += "4"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos5, self.h5, self.v5) == True:
            self.num += "5"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos6, self.h6, self.v6) == True:
            self.num += "6"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos7, self.h7, self.v7) == True:
            self.num += "7"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos8, self.h8, self.v8) == True:
            self.num += "8"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.pos9, self.h9, self.v9) == True:
            self.num += "9"
            time.sleep(2*self.sleep_time)
        if hoverclick(self.posd, self.hd, self.vd) == True:
            self.num += "."
            time.sleep(2*self.sleep_time)
        if hoverclick(self.posm, self.hm, self.vm) == True:
            if len(self.num) !=0 and self.num[0] == "-":
                self.num = ""
            else:
                self.num = "-" + self.num
            time.sleep(2*self.sleep_time)
            
    # --------------------------------------------------------------------------------------------
    # DRAWING FUNCTIONS
    # --------------------------------------------------------------------------------------------
    
    def draw_commands(self, ):
        # throws up a number entry screen.
        mx, my = pg.mouse.get_pos() # mouse coordinates for interactivity

        # position of calculator
        # Rectangle initialized from the top left corner.
        # horizontal and vertical dimensions
        h = 0.47*self.game.sx
        v = 0.5*self.game.sy

        def command_disp(string, pos, h, v, mx, my, game, font=20, extra=None):
            displayfont = pygame.font.Font('freesansbold.ttf', font) # font        
            disp = displayfont.render(string, True, GREEN, BLACK)
            displayRect = disp.get_rect()
            displayRect.center = (pos[0]+0.55*h, pos[1]+0.7*v)
            game.display.blit(disp, displayRect)                
        
        def command_button(string, pos, h, v, mx, my, game, message, font=20, extra=None):
            buttonfont = pygame.font.Font('freesansbold.ttf', 18) # font
            if (mx > pos[0] and mx < pos[0]+h) and (my > pos[1] and my < pos[1]+v):
                button = buttonfont.render(string, True, GREEN, BLACK)                
                command_disp(message, (0.68*self.game.sx, 0.2*self.game.sy), h, v, mx, my, game)
                if extra!=None:
                    for i in range(len(extra)):
                        command_disp(extra[i],
                                     (0.68*self.game.sx, (0.25 + 0.05*i)*self.game.sy),
                                     h,
                                     v,
                                     mx,
                                     my,
                                     game)
            else:
                button = buttonfont.render(string, True, NEONGREEN, BLACK)
                
            buttonRect = button.get_rect()
            buttonRect.width = h
            buttonRect.height = v
            buttonRect.center = (pos[0]+0.55*h, pos[1]+0.7*v)
            
            pg.draw.rect(game.display, NEONGREEN, (pos[0],pos[1], 1.08*h, 1.01*v), 1)
            game.display.blit(button, buttonRect)

        tonmess = "View the problem." 
        tonmess = "Turn the laser on."
        tofmess = "Turn the laser off."
        paumess = "Pause the laser for a given time."
        intmess = "Set the intensity of the laser."
        movmess = "Move the laser along the grid."
        extramov = ["Positive input: move clockwise.",
                    "Negative input: move anticlockwise"]
        orimess = "Orient the laser."
        formess = "Begin FOR loop."
        efomess = "End FOR loop."
        delmess = "Delete the previous line."
        graphmess = "Switch to the laser screen."
        submess = ">> SUBMIT <<"
        quitmess = "Return to the menu screen."
        command_button(" TURN ON", self.tonpos, self.hton, self.vton, mx, my, self.game, tonmess)
        command_button("TURN OFF", self.tofpos, self.htof, self.vtof, mx, my, self.game, tofmess)
        command_button("   PAUSE", self.paupos, self.hpau, self.vpau, mx, my, self.game, paumess)
        command_button("INTENSITY", self.intpos, self.hint, self.vint, mx, my, self.game, intmess)
        command_button("    MOVE", self.movpos, self.hmov, self.vmov, mx, my, self.game, movmess, extra=extramov)
        command_button("   ORIENT", self.oripos, self.hori, self.vori, mx, my, self.game, orimess)
        if self.foron == 1:
            command_button("END LOOP", self.forpos, self.hfor, self.vfor, mx, my, self.game, efomess)
        else:
            command_button("    LOOP", self.forpos, self.hfor, self.vfor, mx, my, self.game, formess)
            
        command_button("   DELETE", self.backpos, self.hback, self.vback, mx, my, self.game, delmess)        
        command_button("   SWITCH", self.graphpos, self.hgraph, self.vgraph, mx, my, self.game, graphmess)
        command_button("   SUBMIT", self.subpos, self.hsub, self.vsub, mx, my, self.game, submess)
        command_button("  QUIT", self.quitpos, self.hquit, self.vquit, mx, my, self.game, quitmess)

        warnfont = pygame.font.Font('freesansbold.ttf', 10) # font        
        warn1 = warnfont.render("WARNING!", True, GREEN, BLACK)
        warn2 = warnfont.render("Once program starts", True, GREEN, BLACK)
        warn3 = warnfont.render("it can't be stopped!", True, GREEN, BLACK)
        
        warn1Rect = warn1.get_rect()
        warn2Rect = warn2.get_rect()
        warn3Rect = warn3.get_rect()
        
        warn1Rect.center = (self.subpos[0]+0.067*self.game.sx, self.subpos[1]+0.1*self.game.sy)
        warn2Rect.center = (self.subpos[0]+0.067*self.game.sx, self.subpos[1]+0.13*self.game.sy)
        warn3Rect.center = (self.subpos[0]+0.067*self.game.sx, self.subpos[1]+0.155*self.game.sy)
        
        self.game.display.blit(warn1, warn1Rect)
        self.game.display.blit(warn2, warn2Rect)
        self.game.display.blit(warn3, warn3Rect) 
        
    def draw_numbers(self,):
        # throws up a number entry screen.
        mx, my = pg.mouse.get_pos() # mouse coordinates for interactivity
        
        # position of calculator
        # Rectangle initialized from the top left corner.
        # horizontal and vertical dimensions
        h = 0.47*self.game.sx
        v = 0.5*self.game.sy

        def disp(string, pos, h, v, x, y, game):
            displayfont = pygame.font.Font('freesansbold.ttf', 40) # font        
            disp = displayfont.render(string, True, GREEN, BLACK)
            displayRect = disp.get_rect()
            displayRect.center = (pos[0]+0.55*h, pos[1]+0.7*v)
            game.display.blit(disp, displayRect)              

        def button(string, pos, h, v, mx, my, x, y, game):
            buttonfont = pygame.font.Font('freesansbold.ttf', 18) # font            
            if (mx > pos[0] and mx < pos[0]+h) and (my > pos[1] and my < pos[1]+v):
                button = buttonfont.render(string, True, GREEN, BLACK)

            else:
                button = buttonfont.render(string, True, NEONGREEN, BLACK)

            buttonRect = button.get_rect()
            buttonRect.width = h
            buttonRect.height = v
            buttonRect.center = (pos[0]+0.55*h, pos[1]+0.7*v)
            
            pg.draw.rect(game.display, NEONGREEN, (pos[0],pos[1], 1.08*h, 1.01*v), 1)
            game.display.blit(button, buttonRect)

        
        # the stage for the calculator
        pg.draw.rect(self.game.display, BLACK, (self.cx,self.cy, h,v), 0)
        pg.draw.rect(self.game.display, NEONGREEN, (self.cx,self.cy-0.02*self.game.sy,h,0.99*v), 1)
        pg.draw.rect(self.game.display, NEONGREEN, (self.cx+0.01*self.game.sx,
                                                    self.cy+0.01*self.game.sy,
                                                    0.96*h,
                                                    0.2*v), 1)

        # number keys
        button(" ENTER", self.entpos, self.enth, self.entv, mx, my, self.cx, self.cy, self.game)
        button("DELETE", self.delpos, self.delh, self.delv, mx, my, self.cx, self.cy, self.game)  
        button("CANCEL", self.canpos, self.canh, self.canv, mx, my, self.cx, self.cy, self.game)  
        button(" 0", self.pos0, self.h0, self.v0, mx, my, self.cx, self.cy, self.game)
        button(" 1", self.pos1, self.h1, self.v1, mx, my, self.cx, self.cy, self.game)
        button(" 2", self.pos2, self.h2, self.v2, mx, my, self.cx, self.cy, self.game)
        button(" 3", self.pos3, self.h3, self.v3, mx, my, self.cx, self.cy, self.game)
        button(" 4", self.pos4, self.h4, self.v4, mx, my, self.cx, self.cy, self.game)
        button(" 5", self.pos5, self.h5, self.v5, mx, my, self.cx, self.cy, self.game)
        button(" 6", self.pos6, self.h6, self.v6, mx, my, self.cx, self.cy, self.game)
        button(" 7", self.pos7, self.h7, self.v7, mx, my, self.cx, self.cy, self.game)
        button(" 8", self.pos8, self.h8, self.v8, mx, my, self.cx, self.cy, self.game)
        button(" 9", self.pos9, self.h9, self.v9, mx, my, self.cx, self.cy, self.game)
        button(" .", self.posd, self.hd, self.vd, mx, my, self.cx, self.cy, self.game)
        button(" -", self.posm, self.hm, self.vm, mx, my, self.cx, self.cy, self.game)        
        
        # this displays the typed string on the bar
        disp(self.num,
             (self.cx+0.1*self.game.sx, self.cy+0.03*self.game.sy),
             0.04*self.game.sx,
             0.05*self.game.sy,
             self.cx,
             self.cy,
             self.game)
                

    #--------------------------------------------------------------------------------------

    def draw_highlevel(self,):
        # This is intended to display the program in terms of a high level language.
        def line_disp(string, pos, game):
            displayfont = pygame.font.Font('freesansbold.ttf', 14) # font        
            disp = displayfont.render(string, True, GREEN, BLACK)
            displayRect = disp.get_rect()
            displayRect.left = 0.4*self.game.sx
            displayRect.center = (pos[0], pos[1])
            game.display.blit(disp, displayRect)

        for i in range(len(self.high_level)):
            line_disp(self.high_level[i],
                      (0.25*self.game.sx,
                       (0.1+0.05*i)*self.game.sy),
                      self.game)

    
    # ------------------------------------------------------------------------------------------
    # LEAD FUNCTIONS
    # ------------------------------------------------------------------------------------------
    
    def UpdateInterface(self,):        
        if self.num_entry == True:
            self.number_input()
        else:
            self.command_input()
    
    def DrawInterface(self,):
        # The interface is intended to resemble an old-school terminal.
        # Black background, green text and buttons.
        # Have the words flashing across the screen as though they're being typed.
        self.game.display.fill(BLACK)
        pg.draw.line(self.game.display,
                     NEONGREEN,
                     (self.game.sx//2, 0),
                     (self.game.sx//2, self.game.sy))
        
        self.draw_highlevel()
        self.draw_commands()        
        if self.num_entry == True:
            self.draw_numbers()

