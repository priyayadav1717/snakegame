from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("blue")
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.penup()
        self.hideturtle()
    def reset(self) :
        if self.score> self.high_score:
            self.high_score = self.score
            with open("data.txt",  mode = "w") as file:
                self.high_score= file.write(f"{self.score}")
        self.score = 0
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 28, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score : {self.high_score}", align="center", font=("Arial", 28, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
