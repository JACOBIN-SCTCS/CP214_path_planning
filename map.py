import pygame
from pygame.locals import *
import random
import numpy as np

class RRTStar:

    def __init__(self,numObstacles = 30):
        pass


class Map:

    def __init__(self,wH=640,wW=480):
        
        self.screen = pygame.display.set_mode((wH,wW))
        self.screen.fill((255,255,255))
        self.obstacle_color = (128,128,128)

        self.rrt_star  = RRTStar()

    def drawObstacles(self,obstacles):
        pass





