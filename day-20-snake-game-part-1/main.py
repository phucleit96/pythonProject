from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Phuc's Snake Game")
screen.setup(width=600, height=600)
# initiate the 3 first body block

screen.tracer(0) #turn the delay off, read the documentation turtle

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()  # retrigger the animation of the snake body
    time.sleep(0.1)
    snake.move()

    #Detect collision with food --> distance(), read documentation for more,
    # <15 is the ideal distance for collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.eat()

    #Detect collision with wall, square 300 300, head = 20 --> deduction
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #Detect collision with tails:
    #if head collides with any segment in the tail --> trigger gameover()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()