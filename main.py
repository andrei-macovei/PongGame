import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

LEFT_PADDLE_X = -450
LEFT_PADDLE_Y = 0
RIGHT_PADDLE_X = 450
RIGHT_PADDLE_Y = 0


def main():
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong Evolved")
    screen.tracer(0)
    screen.register_shape("paddle", ((-5, 30), (-5, -30), (5, -30), (5, 30)))

    # Draw middle line
    line = Turtle()
    line.goto(0, -SCREEN_HEIGHT)
    line.setheading(90)
    line.hideturtle()
    line.pensize(5)
    line.color("white")
    while line.ycor() < SCREEN_HEIGHT:
        if line.isdown():
            line.penup()
        else:
            line.pendown()
        line.forward(20)

    game_is_on = True

    # initialize paddles
    paddle1 = Paddle(LEFT_PADDLE_X, LEFT_PADDLE_Y)
    paddle2 = Paddle(RIGHT_PADDLE_X, RIGHT_PADDLE_Y)

    ball = Ball()

    score_player_left = Score(-60, SCREEN_HEIGHT/2 - 70)
    score_player_right = Score(60, SCREEN_HEIGHT/2 - 70)

    screen.listen()
    screen.onkey(paddle1.up, "w")
    screen.onkey(paddle1.down, "s")
    screen.onkey(paddle2.up, "Up")
    screen.onkey(paddle2.down, "Down")

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect ball collision with walls
        if ball.ycor() > (SCREEN_HEIGHT/2 - 10) or ball.ycor() < -(SCREEN_HEIGHT/2 - 10):
            ball.manage_wall_collision()

        # Detect ball collsion with paddle
        if (ball.distance(paddle1) < 30 and ball.xcor() <= LEFT_PADDLE_X + 10) or \
                (ball.distance(paddle2) < 30 and ball.xcor() >= (RIGHT_PADDLE_X - 10)):
            ball.manage_paddle_collision()

        # Detect if ball is behind any paddle
        if ball.xcor() < LEFT_PADDLE_X - 30 or ball.xcor() > RIGHT_PADDLE_X + 30:
            if ball.xcor() < LEFT_PADDLE_X - 30:
                score_player_right.increase_score()
            else:
                score_player_left.increase_score()
            ball.refresh()
            paddle1.refresh(LEFT_PADDLE_X, LEFT_PADDLE_Y)
            paddle2.refresh(RIGHT_PADDLE_X, RIGHT_PADDLE_Y)
            time.sleep(2)

    screen.exitonclick()


if __name__ == '__main__':
    main()
