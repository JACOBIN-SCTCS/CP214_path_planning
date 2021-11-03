import pygame
from pygame.locals import *
import math
import random
import sys
import numpy as np

class RRTStar:
    def __init__(self,W,H,screen,numObstacles = 30):
        self.obstacles = []
        self.nObstacles = numObstacles
        self.obstacle_dim = 20
        self.window_width = W
        self.window_height = H
        self.starting_point = ()
        self.ending_point = ()
        self.num_iterations  = 1000
        self.steer_distance = 35
        self.rewire_radius = 7
        self.screen =screen
        self.x = []
        self.y = []
        self.distance = [] 
        self.parent = []


    def generate_obstacles(self):
        x_coord = np.random.randint(0,self.window_height-self.obstacle_dim,self.nObstacles).tolist()
        y_coord = np.random.randint(0,self.window_width-self.obstacle_dim,self.nObstacles).tolist()
        
        for i in range(len(x_coord)):
            obstacle = Rect(x_coord[i],y_coord[i],self.obstacle_dim,self.obstacle_dim)
            self.obstacles.append(obstacle)

    def get_nearest_node_idx(self,x,y):
        distance = (self.x[0]-x)*(self.x[0]-x) + (self.y[0]-y)*(self.y[0]-y)
        nearest_node_idx = 0
        for i in range(len(self.x)):
            cur_distance = (self.x[i]-x)*(self.x[i]-x) + (self.y[i]-y)*(self.y[i]-y)
            if (cur_distance< distance):
                distance = cur_distance
                nearest_node_idx = i
        return nearest_node_idx

    def rewire():
        pass


    def start_planning(self):
        self.x.append(self.starting_point[0])
        self.y.append(self.starting_point[1])
        self.distance.append(0)
        self.parent.append(-1)

        t=0
        while(t<self.num_iterations):
            x_rand = np.random.randint(0,self.window_height)
            y_rand = np.random.randint(0,self.window_width)
            
            idx = self.get_nearest_node_idx(x_rand,y_rand)
            
            #candidate_node=[x_rand,y_rand]

            dist = (x_rand-self.x[idx])*(x_rand-self.x[idx]) + (y_rand-self.y[idx])*(y_rand-self.y[idx])
            x_steer = 0
            y_steer = 0

            if(dist<=(self.steer_distance*self.steer_distance)):
                x_steer = x_rand
                y_steer = y_rand
            else:
                angle = math.atan2(y_rand-self.y[idx],x_rand-self.x[idx])
                x_steer = int(self.x[idx] + self.steer_distance*math.cos(angle))
                y_steer = int(self.y[idx]+ self.steer_distance*math.sin(angle))
                dist = self.steer_distance 

            obstacle_collide = False
            for obstacle in self.obstacles:
                if(obstacle.collidepoint((x_steer,y_steer))):
                    obstacle_collide = True
                    break
            if(obstacle_collide):
                continue
            
            obstacle_edge = False
            for i in range(0,200):
                u = i/200  
                x_line = int((u*self.x[idx])+((1-u)*x_steer))
                y_line = int((u*self.y[idx])+((1-u)*y_steer))

                for obstacle in self.obstacles:
                    if(obstacle.collidepoint((x_line,y_line))):
                        obstacle_edge = True
                        break
                if(obstacle_edge):
                    break
            
            if(not obstacle_edge):
                self.x.append(x_steer)
                self.y.append(y_steer)
                self.parent.append(idx)
                self.distance.append(math.sqrt(dist))
                pygame.draw.circle(self.screen,(0,0,0),(x_steer,y_steer),2)
                pygame.draw.line(self.screen,(0,0,0),(self.x[idx],self.y[idx]),(x_steer,y_steer))
                pygame.display.update()
            t+=1

    def set_start_end_point(self,start,end):
        for obstacle in self.obstacles:
            if obstacle.collidepoint(start) or obstacle.collidepoint(end):
                print("Collision Detected")
                pygame.quit()
                sys.exit()
        
        self.starting_point = start
        self.ending_point = end
        self.start_planning()
    

class Map:

    def __init__(self,wH=640,wW=480):
        
        self.screen = pygame.display.set_mode((wH,wW))
        self.screen.fill((255,255,255))
        self.obstacle_color = (128,128,128)
        self.starting_point_color = (255,0,0)
        self.ending_point_color = (0,255,0)
        self.rrt_star  = RRTStar(wW,wH,self.screen)

    def set_starting_ending_point(self,start,end):
        self.rrt_star.set_start_end_point(start,end) 

    def drawObstacles(self):
        self.rrt_star.generate_obstacles()
        for obstacle in self.rrt_star.obstacles:
            pygame.draw.rect(self.screen,self.obstacle_color,obstacle)
        




