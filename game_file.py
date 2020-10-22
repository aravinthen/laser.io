# Program Name: game_file.py
# Author: Aravinthen Rajkumar
# Description: Aravinthen Rajkumar

import pygame as pg
import math as m
import os

pg.init()

class LaserGame:
    
    class Pixel:
        def __init__(self, x, y, vx, vy, mat):
            self.x = x
            self.y = y
            self.vx = vx
            self.vy = vy
            self.mat = mat

            if mat == 'solid':
                pg.image.load('./images/pixel.png')

    class Laser:
        def __init__(self, x, y, angle):
            self.x = x
            self.y = y            
            self.angle = angle # direction the laser is pointing.
                               # represents rotation matrix

            self.phase = 1     # this is an animation quirk
                               # the phase rapidly changes as frame is updated
            
            self.onoff = False # sets the status of the laser as ON or OFF
                               # ON: True
                               # OFF: False
                               
            self.image = pg.image.load('./images/monster.png')

    def __init__(self, bx, by, speed):        
        self.bound_x = bx
        self.bound_y = by
        self.speed = speed
        self.pixel_list = [] # empty pixel list
                             # will be used to hold material pixels

        self.laser = self.Laser(500,400,0) # Initial position and angle of the laser
        
        self.clock = pg.time.Clock()
        size = (1000,800)
        self.screen = pg.display.set_mode(size)

    def update_laser(self, new_pos, new_angle):
        # set a new position or direction vector here.
        self.laser.x = new_pos[0]
        self.laser.y = new_pos[1]
        self.laser.angle = new_angle

    def update_materials(self):
        # NOT IMPLEMENTED YET
        # update the position of the material pixels
        for p in self.pixel_list:
            p.x = p.x + p.vx*self.speed
            p.y = p.y + p.vy*self.speed
            
            if (p.x > self.bound_x or p.x < 1):
                p.col +=1
                p.vx = -p.vx
            if (p.y > self.bound_x or p.y < 1):
                p.col +=1
                p.vy = -p.vy
                
            if p.col > 3:
                self.pixel_list.remove(p)
                
    def write(self):
        # dumps all the content that needs to be visualized onto the screen.
        if self.laser.onoff == True:
            # note the skew required to align all the images
            start = (self.laser.x+20, self.laser.y+20)
            
            # THIS HAS TO BE CHANGED WHEN THERE'S A COLLISION
            # obviously rotation matrix, probably best to use numpy 
            end = (m.cos(self.laser.angle)*(self.laser.x + 500) + m.sin(self.laser.angle)*(self.laser.y + 500),
                   -m.sin(self.laser.angle)*(self.laser.x + 500) + m.cos(self.laser.angle)*(self.laser.y + 500))

            # cheeky little animation
            # look at it go, damn
            if self.laser.phase == 1:
                pg.draw.line(self.screen, (255,0,0), start, end, 5)
            if self.laser.phase == -1:
                pg.draw.line(self.screen, (255,0,0), start, end, 15)

                
        for pixel in self.pixel_list:
            self.screen.blit(pixelImg, (pixel.x, pixel.y))
            
        self.screen.blit(self.laser.image, (self.laser.x, self.laser.y))
            

#--------------------------------------------------------------------------------------------
running = True
step_count = 0


game = LaserGame(1000, 800, 1)

# arg1: x position
# arg2: y position
# arg3: direction the laser faces

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    

    # pixel position
    if event.type == pg.MOUSEBUTTONDOWN:
        game.laser.onoff = True # draw a line representing the laser
        game.laser.phase = -game.laser.phase
    else:
        game.laser.onoff = False

    # update state of the program
    game.update_materials()

    # update the background    
    game.screen.fill((0,0,0)) # drawing the sceen all over again
    game.update_laser((game.laser.x, game.laser.y), game.laser.angle+0.01)    
    game.write()
    
    pg.display.update()
    step_count += game.speed

    game.clock.tick(200)
    
pg.quit()



    
    
