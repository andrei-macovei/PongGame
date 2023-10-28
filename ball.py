from turtle import Turtle
import random

POSSIBLE_HEADINGS = [45, 135, 225, 315]

START_MOVE_SPEED = 0.2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.speed("fastest")
        self.refresh()
        self.move_distance = START_MOVE_SPEED

    def move(self):
        self.forward(self.move_distance)

    def manage_wall_collision(self):
        self.setheading(self.heading() + 90 % 360)

    def manage_paddle_collision(self):
        self.setheading(self.heading() - 90 % 360)
        self.move_distance *= 1.1

    def refresh(self):
        self.goto(0, random.randint(-250, 250))
        self.setheading(random.choice(POSSIBLE_HEADINGS))
        self.move_distance = START_MOVE_SPEED
