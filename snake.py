from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for positions in POSITION:
            self.add_segment(positions)

    def add_segment(self,positions):
        new_snakes = Turtle("square")
        new_snakes.color("white")
        new_snakes.penup()
        new_snakes.goto(positions)
        self.segment.append(new_snakes)


    def extend(self):
        self.add_segment(self.segment[-1].position())




    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):

            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)



    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def lefts(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
