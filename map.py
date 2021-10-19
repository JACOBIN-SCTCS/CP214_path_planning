import pygame
from pygame.locals import *
import random
import numpy as np

class RRTStar:

    def __init__(self,W,H,numObstacles = 30):
        self.obstacles = []
        self.nObstacles = numObstacles
        self.window_width = W
        self.window_height = H

    def generate_obstacles(self):
        x_coord = np.random.randint(0,self.window_width,self.nObstacles).tolist()
        y_coord = np.random.randint(0,self.window_height,self.nObstacles).tolist()
        
        for i in range(len(x_coord)):
            self.obstacles.append((x_coord[i],y_coord[i]))


class Map:

    def __init__(self,wH=640,wW=480):
        
        self.screen = pygame.display.set_mode((wH,wW))
        self.screen.fill((255,255,255))
        self.obstacle_color = (128,128,128)
        self.rrt_star  = RRTStar(wW,wH)


    def drawObstacles(self):
        self.rrt_star.generate_obstacles()
        
        for coord in self.rrt_star.obstacles:
            pygame.draw.circle(self.screen,self.obstacle_color,coord,7)
            #print(coord)




