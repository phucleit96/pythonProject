from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Who is your choice to win the race? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# trigger new list to containt the new object: 6 turtles:
all_turtles = []
y_position = [-150, -120, -90, -60, -30, 0]
# x = colors.index("red")
#position = [-230, -150]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.up()
    #new_turtle.goto(position)
    new_turtle.speed("fastest")
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    #position[1] += 30
    all_turtles.append(new_turtle)
    #   x += 1

if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtles:
        if each_turtle.xcor() > 230:
            is_race_on = False
            winning_color = each_turtle.pencolor()
            if user_bet == winning_color:
                print("Your guess is right, you won!")
            else:
                print(f"Your guess is wrong, it should have been {winning_color}, you failed!")
        rand_distance = random.randint(0, 10)
        each_turtle.forward(rand_distance)
#
#
# timblue = Turtle(shape="turtle")
# timblue.color("blue")
# timblue.up()
# timblue.goto(x=-230, y=-120)
#
#
# timyellow = Turtle(shape="turtle")
# timyellow.color("yellow")
# timyellow.up()
# timyellow.goto(x=-230, y=-60)
#
#
# timpurple = Turtle(shape="turtle")
# timpurple.color("purple")
# timpurple.up()
# timpurple.goto(x=-230, y=-90)
#
#
# timgreen = Turtle(shape="turtle")
# timgreen.color("green")
# timgreen.up()
# timgreen.goto(x=-230, y=-30)
#
#
# timorange = Turtle(shape="turtle")
# timorange.color("orange")
# timorange.up()
# timorange.goto(x=-230, y=0)

screen.exitonclick()