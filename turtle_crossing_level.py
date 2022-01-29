# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 03:39:38 2022

@author: wajee
"""

import turtle
from turtle import Screen, Turtle
import time
#import importlib


#importlib.reload(turtle)

class Level(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.level=1
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_Level()
        self.hard=0.1
    
    
    def update_Level(self):
        
        self.write(f"Level : {self.level}",align="center",font=("Arial",24,"normal"))
        
    def game_over(self):
        
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",24,"normal"))
        
    def increase_level(self):
        
        self.level +=1
        self.clear()
        self.update_Level()
    
    def get_level_hardness(self):
        self.hard=(self.hard/10)
        
        