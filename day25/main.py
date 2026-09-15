import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. states game")
image = "day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tim_writer = turtle.Turtle()
tim_writer.hideturtle()
tim_writer.penup()


df = pd.read_csv("day25/50_states.csv")

list_of_states = df["state"].to_list()


# answer_state = screen.textinput(title="Guess the state", prompt="enter state name")
# print(answer_state)

game_is_on = True
correct_state_counter = 0

while game_is_on and correct_state_counter < 50:
    answer_state = screen.textinput(title=f"{correct_state_counter}/50 correct", prompt="enter state name").title()

    if answer_state == "Exit":
        game_is_on = False
    if answer_state in list_of_states:
        
        print("correct guess")
        list_of_states.remove(answer_state)
        correct_state_counter += 1
        tim_writer.goto(df[df["state"]==answer_state].x.item(), df[df["state"]==answer_state].y.item())
        tim_writer.write(answer_state)
     

    
new_data = pd.DataFrame(list_of_states)
new_data.to_csv("day25/missing_states_toLearn.csv")


# if answer_state.title() in list_of_states:
#     tim_writer.goto(df[df["state"]==answer_state].x, df[df["state"]==answer_state].y)
#     tim_writer.write(answer_state)
#     print("yes")








screen.exitonclick()