# Program Name: game_file.py
# Author: Aravinthen Rajkumar
# Description: Aravinthen Rajkumar

import pygame as pg
import os

pg.init()

size = (1000,800)
clock = pg.time.Clock()
screen = pg.display.set_mode(size)

# images
monsterImg = pg.image.load('images/monster.png')
pixelImg = pg.image.load('images/pixel.png')

def monster(x,y):
    screen.blit(monsterImg, (x,y))

class activePixels:
    
    class Pixel:
        def __init__(self, x, y, vx, vy):
            self.x = x
            self.y = y
            self.vx = vx
            self.vy = vy
            self.col = 0

    def __init__(self, bx, by, speed):        
        self.bound_x = bx
        self.bound_y = by
        self.speed = speed
        self.pixel_list = [] # empty pixel list

    def gen_pixel(self, x, y, vx, vy):                    
        # generates a pixel of a particular type.
        pix = self.Pixel(x, y, vx, vy)
        self.pixel_list.append(pix)
        
    def update(self):
        
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
        for pixel in self.pixel_list:
            screen.blit(pixelImg, (pixel.x, pixel.y))
            

#--------------------------------------------------------------------------------------------
running = True
step_count = 0
x_dir = 1
y_dir = 1

x=50
y=50
speed = 1

pixels = activePixels(1000, 800, 10)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    

    if x > 1000 or x < 1:
        x_dir = -x_dir
    if y > 800 or y < 1:
        y_dir = -y_dir

    # monster position
    x += x_dir
    y += y_dir        
    screen.fill((0,0,0)) # this is required, we're just drawing the sceen all over again

    # pixel position
    if event.type == pg.MOUSEBUTTONDOWN:
        pixels.gen_pixel(x,y,1,0)

    monster(x,y)
    pixels.update()
    pixels.write()
    pg.display.update()
    step_count+=speed
    
    clock.tick(200)
    
pg.quit()



    
    
