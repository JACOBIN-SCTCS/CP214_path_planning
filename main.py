import pygame 
from pygame.locals import *
import sys
from map import Map
starting_chosen = False
ending_chosen = False
starting_point = ()
ending_point = ()

pygame.init()
pygame.font.init()

m = Map()
m.drawObstacles()

while True:
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == MOUSEBUTTONUP:
            #print(pygame.mouse.get_pos())
            if(not starting_chosen):
                starting_chosen = True
                starting_point = pygame.mouse.get_pos()
                pygame.draw.circle(m.screen,m.starting_point_color,starting_point,7)
            else:
                if(not ending_chosen):
                    ending_chosen = True
                    ending_point = pygame.mouse.get_pos()
                    pygame.draw.circle(m.screen,m.ending_point_color,ending_point,7)
                    m.set_starting_ending_point(starting_point,ending_point)
        elif e.type==QUIT:
            pygame.quit()
            sys.exit()
