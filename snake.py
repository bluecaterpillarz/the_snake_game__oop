from turtle import Turtle

MOVE_DISTANCE=20



class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(-i * 20, 0)
            self.turtles.append(turtle)

    def snake_forward(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            self.turtles[i].goto(self.turtles[i - 1].xcor(), self.turtles[i - 1].ycor())
        self.turtles[0].forward(MOVE_DISTANCE)

    def snake_up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def snake_down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def snake_left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def snake_right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def getting_bigger(self):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(self.turtles[-1].xcor(),self.turtles[-1].xcor())
        self.turtles.append(turtle)

