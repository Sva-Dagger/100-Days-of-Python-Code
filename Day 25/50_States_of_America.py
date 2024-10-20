import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
missing_states=[]
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt=f"{len(guessed_states)}/50 what's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [missing_states.append(states) for states in all_states if states not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t =  turtle.Turtle()
        t.hideturtle()
        t.penup()
        State_data = data[data.state == answer_state]
        t.goto(int(State_data.x), int(State_data.y))
        t.write(State_data.state.item())