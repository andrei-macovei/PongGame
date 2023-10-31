from turtle import Turtle
import random

POSSIBLE_HEADINGS = [45, 135, 225, 315]

START_MOVE_SPEED = 0.02


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.refresh()
        self.move_speed = START_MOVE_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def manage_wall_collision(self):
        # self.setheading(self.heading() + 90 % 360)
        self.y_move *= -1   # change direction on y-axis

    def manage_paddle_collision(self):
        # self.setheading(self.heading() - 90 % 360)
        self.x_move *= -1   # change direction on x-axis
        self.move_speed *= 0.9
        # print(f"Ball move speed:{self.move_speed}")

    def refresh(self):
        self.goto(0, random.randint(-250, 250))
        # self.setheading(random.choice(POSSIBLE_HEADINGS))
        self.move_speed = START_MOVE_SPEED
        self.manage_paddle_collision()
