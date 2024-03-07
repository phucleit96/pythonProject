import turtle as t
from turtle import Turtle, Screen

import random
import colorgram

rgb_color = []
colors = colorgram.extract("image.jpg", 50)
print(colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    my_tuple = (r, g, b)
    rgb_color.append(my_tuple)

# print(rgb_color)


def random_colo():
    random_color = random.choice(rgb_color)
    return random_color


tim = Turtle()
t.colormode(255)
"""Setting angle downward diagonal"""
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.speed(10)
tim.hideturtle()


def drawing_row():
    for _ in range(10):
        tim.dot(20, random_colo())
        tim.forward(50)


def moving_cursor():
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


for _ in range(10):
    drawing_row()
    moving_cursor()



screen = Screen()
screen.exitonclick()

