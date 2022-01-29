# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 17:16:25 2022

@author: wajee
"""

### Draw a square and move it to the other screen

#INIT_POSITION = (310,0)

import turtle
from turtle import Screen, Turtle
import random

#right_screen_value=random.randint(310, 350)
#INIT_POSITION = (right_screen_value,0)

class Squares(Turtle):
    
    def __init__(self,position,colors):
        
        super().__init__()
        self.color("black")
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.color(colors)
        self.goto(position)
    
    def motion(self):
        
        self.penup()
        new_x = self.xcor() -10
        self.goto(new_x,self.ycor())