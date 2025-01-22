import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
screen.setup(width=700,height=700)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

guessed_states = []

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    if answer_state.lower() == "exit":
        break

    answer_state = answer_state.title()
    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x.item()), int(state_data.y.item()))
        writer.write(answer_state)


screen.exitonclick()
