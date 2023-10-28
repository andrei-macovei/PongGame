from turtle import Turtle


class Score(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto((xcor, ycor))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(self.score, move=False, align="center",
                   font=("Courier", 50, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", move=False, align="center",
                   font=("Courier", 24, "bold"))
