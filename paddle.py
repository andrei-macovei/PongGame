from turtle import Turtle

MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, start_xcor, start_ycor):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shape("paddle")
        self.setheading(90)
        self.goto(start_xcor, start_ycor)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def refresh(self, start_xcor, start_ycor):
        self.goto(start_xcor, start_ycor)
