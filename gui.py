# Program Name: gui.py
# Author: Aravinthen Rajkumar
# Description: Pixel-based graphics of the system.
#              This just builds an array of pixels that can then be given values


import pygame as pg

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
    
    def pixelframe(self):
        #converts the pixel frame defined above into a full frame
        self.screen = pg.display.set_mode([self.X, self.Y])

    def play(self, mode):
        pg.init() # initializes pygame
        game.pixelframe()
        pg.display.set_caption(mode)
        
        clock = pg.time.Clock() # define game clock
        
        running = True
        while running:
            for event in pg.event.get():
                # events are objects corresponding to what the user does on screen
                # print the events to see exactly what's going on there, it's pretty cool m8
                if event.type == pg.QUIT:
                    running = False
            pg.display.update() # could use flip if we're working with pixels?
            clock.tick(60) # controls FPS
            
        pg.quit()
                    

game = PixelArray(800,600)
game.play("plasma")
                
        
