from turtle import Turtle
class Scorecard(Turtle):


    def __init__(self):
        super().__init__()
        self.score=0
        with open("score.text") as text:
            self.high_score=int(text.read())

        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update()
    def update(self):
        self.clear()
        self.write(f"score: {self.score} high score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
    def new_score(self):
        self.score+=1
        self.update()
    def reset(self):
        if self.score  > self.high_score:
           self.high_score=self.score
           with open("score.text", mode="w")as file:
               file.write(f"{self.high_score}")
        self.score=0
        self.update()