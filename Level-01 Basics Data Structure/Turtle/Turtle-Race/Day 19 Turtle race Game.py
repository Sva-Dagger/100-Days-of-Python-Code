from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bed", prompt = "which turtle will win the race? Enter a color : ")
colors = ("red", "orange", "yellow", "green", "blue", "purple")
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    New_turtle = Turtle(shape = "turtle")
    New_turtle.color(colors[turtle_index])
    New_turtle.penup()
    New_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(New_turtle)

is_race_on = True
if user_bet :
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"you've won! the {winning_color} turtle is the winner!")
                is_race_on = False
            else :
                print(f"you've lost! the {winning_color} turtle is the winner!")
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)









screen.exitonclick()