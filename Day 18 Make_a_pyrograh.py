import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

def Draw_Spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.speed("fastest")
        tim.circle(100)
        tim.color(random_colour())
        tim.setheading(tim.heading() + size_of_gap)

Draw_Spirograph(5)

screen = Screen()
screen.exitonclick()