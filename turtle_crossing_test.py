# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 17:32:05 2022

@author: wajee
"""

import turtle
from turtle import Screen, Turtle
import time
import random
import importlib
importlib.reload(turtle)

from turtle_crossing_turtle_test import  my_turtle
from multi_square_test import Squares
from turtle_crossing_level import Level



screen = Screen()
screen.bgcolor("white")
screen.setup(width=800 , height=600)
screen.title("Turtle Crossing")
screen.tracer(0)


init_position = (0,-280)
new_turtle = my_turtle(init_position)
screen.listen()
screen.onkey(new_turtle.go_up,"Up")
screen.onkey(new_turtle.go_down,"Down")
screen.onkey(new_turtle.go_right,"Right")
screen.onkey(new_turtle.go_left,"Left")

level = Level()
color_list = ["red","blue","green","orange","yellow","purple", "black"]
(x_value,y_value)=turtle.screensize()


square_list = []

for i in range(x_value):
    
    random_color = random.choice(color_list)
    
    x_axis=random.randrange(300, 20000,50)
    set_y_pos = random.randrange(-280, 280,30)
    position=(x_axis,set_y_pos)
    square=Squares(position,random_color)
    square_list.append(square)

game_is_on=True

while game_is_on:
    
    time_value = level.hard
    time.sleep(time_value)
    screen.update()
    for small_squares in square_list:
        small_squares.motion()
        
        if small_squares.distance(new_turtle) < 30:
            
            print("Detection")
            level.game_over()
            game_is_on = False
    
    if new_turtle.ycor() > 280 :
        
        new_y=-280
        new_x=0
        new_position=(new_x,new_y)
        new_turtle.goto(new_position)
        level.increase_level()
        level.get_level_hardness()
    
    if new_turtle.xcor() > 380:
        new_turtle.setpos(370,new_turtle.ycor())
    
    if new_turtle.xcor() < -370:
        new_turtle.setpos(-370,new_turtle.ycor())
    
screen.exitonclick()

