# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:47:50 2022

@author: wajee
"""


import turtle
from turtle import Screen, Turtle
import time

class my_turtle(Turtle):
    
    def __init__(self,position):
        
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(position)
    
    
    def go_up(self):
    
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    
    def go_down(self):
    
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)
    
    
    def go_right(self):
    
        new_x=self.xcor()+20
        self.goto(new_x,self.ycor())
    
    def go_left(self):
    
        new_x=self.xcor()-20
        self.goto(new_x,self.ycor())
        
        