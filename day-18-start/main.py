import turtle
from turtle import Turtle, Screen
import random
colors = ["cyan", "purple", "white", "blue", "red", "green", "pink", "yellow", "plum"
          , "violet", "azure", "honeydew", "dark orchid", "light blue", "gold"]
tim = Turtle()
# tim = Turtle()
# tim.shape("triangle")
# tim.color("red")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)

# # from turtle import Turtle
# # tim = Turtle()
# # tom = Turtle()
# # jerry = Turtle()
#
# # import turtle
# # tim = turtle.Turtle()
#
# import turtle as t
# tim = t.Turtle()
#
# import heroes
# print(heroes.gen())
# tim = Turtle()
# tim.shape("triangle")
# tim.color("black")
# def dash():
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#
# for _ in range(15):
#     dash()
"""Tu Duy Dai cua Phuc"""
# tim.shape("triangle")
# num_sides = 3
# for _ in range(10):
#     tim.color(random.choice(colors))
#     moving_step = 1
#     while moving_step <= num_sides:
#         tim.forward(100)
#         angle = 360 / num_sides
#         tim.right(angle)
#         moving_step += 1
#     num_sides += 1
"""Tu Duy Optimal"""
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final = (r, g, b)
    return final
#
#
# tim.speed("fastest")
# tim.pensize(15)
# for _ in range(300):
#     tim.color(random_color())
#     tim.forward(30)
#     a = random.randrange(0, 360, 90)
#     tim.right(a)

tim.speed("fastest")
tim.hideturtle()
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)

draw_spirograph(1)
screen = Screen()
screen.exitonclick()



