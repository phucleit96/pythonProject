STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # block 1 2 3 index 012 constant
from turtle import Turtle
"""self represents the instance of the class. By using the “self”  we can access the 
attributes and methods of the class in python. It binds the attributes with the given arguments."""
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # initiate the segment as blank whenever creating a snake object
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        #creating the snake based on starting locations
        for position in STARTING_POSITIONS:
            self.add_segment(position)
              # initiate the snake body combination
            # [<turtle.Turtle object at 0x000002141C124710>, <turtle.Turtle object at
            # 0x000002141E2AE110>, <turtle.Turtle object at 0x000002141E2AE690>]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)
        # block 1 (index 0) move forward, block 2 (index 1)
        # go to pos block 1, block 3 (index 2) go to pos block 2
        # reverse order, the end will move first, use len(segments) to avoid hard core,
        # -1 because of the index list: 0, ... n-1, stop at 0 and step backward as -1

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position): #position to add the segment
        #generate the snake
        new_segment = Turtle(shape="square")
        new_segment.up()
        new_segment.goto(position)
        new_segment.color("white")
        self.segments.append(new_segment)

    def extend(self): #add new segment to snake, need to determine the position of the new
        self.add_segment(self.segments[-1].position()) #last segment

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


