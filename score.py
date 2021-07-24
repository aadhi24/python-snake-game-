from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.times = 0.2
        self.write(f"score {self.scores}", align="center", font=("Aral", 24, "normal"))

    def current_score(self):
        self.clear()
        self.scores += 1
        self.write(f'score {self.scores}', align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write('game Over', align="center", font=("Arial", 28, "normal"))
