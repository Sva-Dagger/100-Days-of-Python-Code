from turtle import Turtle, Screen
import random

timmy = Turtle()

colours = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angles = 360/num_sides
        timmy.forward(100)
        timmy.right(angles)

for shape_side_n in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shape(shape_side_n)





screen = Screen()
screen.exitonclick()