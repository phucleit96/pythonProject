import turtle
from turtle import Turtle
import pandas as pd
import csv
ALIGNMENT = "left"
FONT = ("Arial", 8, "normal")


screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
score = 0
correct_guess = []


# def locate(name, x_position, y_position):
#     state = Turtle()
#     state.hideturtle()
#     state.penup()
#     state.goto(x_position, y_position)
#     state.write(align=ALIGNMENT, font=FONT, arg=name)
#
#
#
# df = pd.read_csv("50_states.csv")
# state_list = df["state"].to_list()
# # locate("Iowa", 38, 65)
# # locate("Montana", -141, 150)
# # locate("Ohio", 176, 52)
# # locate("Arizona", -203, -40)
#
# while game_is_on:
# # def get_mouse_click_coor(x, y):
# #     print(x, y)
# # turtle.onscreenclick(get_mouse_click_coor)
#     answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")
#     guess = answer_state.title()
#     for state_name in state_list:
#         if state_name == guess and score != 50:
#             x_pos = int(df[df.state == state_name].x)
#             y_pos = int(df[df.state == state_name].y)
#             locate(name=state_name, x_position=x_pos, y_position=y_pos)
#             score += 1
#             correct_guess.append(state_name)
#         if score == 50:
#             game_is_on = False
#             print("You Win!")


df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()

while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 "
                                          f"States Correct", prompt="What's another state's name?").title()
    # If answer_state is one of the states in all the states of the 50 states:
    if answer_state == "Exit":
        missing_states = [state_name for state_name in all_states if state_name not in correct_guess]
        missing_x = [df[df.state == missing_state].x.item() for missing_state in missing_states]
        missing_y = [df[df.state == missing_state].y.item() for missing_state in missing_states]
        missing_dic = {"state": missing_states,
                       "x": missing_x,
                       "y": missing_y
                       }
        new_data = pd.DataFrame(missing_dic)
        new_data.to_csv("States to learn.csv")
        break #ending while loop prematurely
    if answer_state in all_states: #only works with lists
        correct_guess.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item()) #item() returns first scalar
        # If they got it right:
            # Create a turtle to write the name of the state at the state's x and y

# states_to_learn.csv
# states_to_learn = []
# x_to_learn = []
# y_to_learn = []
#
# learn_state_dic = {
#     "state": states_to_learn,
#     "x": x_to_learn,
#     "y": y_to_learn
# }
#
# states_to_learn = []
# for state in all_states:
#     if state not in correct_guess:
#         states_to_learn.append(state)
#         x_to_learn.append(int(df[df.state == state].x))
#         y_to_learn.append(int(df[df.state == state].y))
# final = pd.DataFrame(learn_state_dic)
# final.to_csv("states_to_learn.csv")

# names = ["Alex", "Beth", 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
# students_scores = {name:random.randint(1, 10) for name in names}
