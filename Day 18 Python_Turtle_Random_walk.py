import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

colours = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)

for _ in range(200):
    tim.color(random_colour())
    tim.forward(30)
    tim.setheading(random.choice(directions))






screen = Screen()
screen.exitonclick()