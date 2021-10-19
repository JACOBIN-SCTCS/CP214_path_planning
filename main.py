import pygame 
from pygame.locals import *
import sys
from map import Map

pygame.init()
m = Map()
m.drawObstacles()

while True:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())

        elif e.type==QUIT:
            pygame.quit()
            sys.exit()
