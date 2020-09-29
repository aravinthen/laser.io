# Program Name: gui.py
# Author: Aravinthen Rajkumar
# Description: Pixel-based graphics of the system.
#              This just builds an array of pixels that can then be given values


import pygame as pg
import lasercontrollang as lcl

class PixelArray:
    # the full array
    
    class Pixel:
        # a single pixel
        def __init__(self, x, y):
            self.x = x # x-index
            self.y = y # y-index
            self.color = (255,255,255) # default is white

                    
    def __init__(self, X, Y):
        self.X = X # total pixels in x-length
        self.Y = Y # total pixels in y-length                       
        self.Pixels = [self.Pixel(i,j) for i in range(X) for j in range(Y)]
        self.running = False
    
    #-------------------------------------------------------------------------
    # THE MAIN FUNCTION HERE
    def play(self, mode):
        # "plasma" is the first game mode.
        # Depending on how this goes, it'd be nice to introduce other game modes too.
        # "fluid", "alloy" or, dare I say, "polymer"
        
        pg.init() # initializes pygame
        
        if mode == "plasma":
            pg.display.set_caption("Laser Control Programming")    
            l = lcl.LaserControlLanguage() # the main programming language bit
            s = lcl.LaserControlLanguage() # this will be used as a subspace for functions            

        self.screen = pg.display.set_mode([self.X, self.Y])
        
        clock = pg.time.Clock() # define game clock
        running = True
        while running:
            for event in pg.event.get():
                # events are objects corresponding to what the user does on screen
                # print the events to see exactly what's going on there, it's pretty cool m8
                # print(event)
                if event.type == pg.QUIT:
                    running = False
                    
            pg.display.update() # could use flip if we're working with pixels?
            clock.tick(30) # controls FPS
                   
        pg.quit()
                    

game = PixelArray(800,600)
game.play("plasma")
                
        
