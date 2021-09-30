
import pygame
import pygame.gfxdraw
import random
import datetime
import math
import colorsys
import numpy as np
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
middlex = 500
middley = 500
matrix = np.empty((1000,1000))
colors = [(0,0,0),(69, 5, 71),(255,0,0),(0,255,0),(0,0,255), (255,0,255), (0,255,255), (255,255,0), (255, 150, 0), (50, 150, 200)]
def rainbow():
    h1 = colorsys.hsv_to_rgb((((math.ceil((datetime.datetime.now().timestamp() * 1000) / 20)) / 360)), 1, 1)
    (r, g, b) = h1
    r*=255
    g*=255
    b*=255
    r = round(r)
    g = round(g)
    b = round(b)
    return (r, g, b)

def direction(x, y):
    result = ""
    if x == 0 and y == 0:
        result = "None"
    if x == 0 and y == 1:
        result = "NORTH"
    if x == 0 and y == -1:
        result = "SOUTH"
    if x == 1 and y == 0:
        result = "EAST"
    if x == -1 and y == 0:
        result = "WEST"
    if x == 1 and y == 1:
        result = "NORTH-EAST"
    if x == -1 and y == 1:
        result = "NORTH-WEST"
    if x == 1 and y == -1:
        result = "SOUTH-EAST"
    if x == -1 and y == -1:
        result = "NORTH-WEST"
    return result
        

def walker(biome):
    global middlex
    global middley
    global matrix
    oldx = middlex
    oldy = middley
    xVel = 0
    yVel = 0
    xVel = random.randrange(-1, 2)
    yVel = random.randrange(-1, 2)
    yVel *= random.randrange(0, 30)
    xVel *= random.randrange(0, 30)
    if not middlex + xVel > 1000 or not middlex + xVel < 0:
        middlex += xVel
    if not middley + yVel > 1000 or not middley + yVel < 0:
        middley += yVel
    if middlex > 0 and middlex < 1000 and middley > 0 and middley < 1000:
        matrix[middlex][middley] = biome
    #print(xVel, yVel)
    #print(direction(xVel, yVel))
    
    #pygame.draw.line(screen, rainbow(), (oldx, oldy), (middlex, middley), 8)
    #pygame.draw.circle(screen, (255,255,255), (middlex, middley), 4)
    
    


while True:
    for nevr in range(100000):
        walker(random.randrange(0,10))
    for a in range(1000):
        for b in range(1000):
            if not matrix[a][b]==0:
                pygame.draw.circle(screen, colors[int(matrix[int(a)][int(b)])], (a, b), 4)
    pygame.display.flip()
      
    
pygame.quit()
