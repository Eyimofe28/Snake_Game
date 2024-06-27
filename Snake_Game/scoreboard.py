from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("savedHighScore.txt", mode='r') as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.speed(0)
        self.penup()
        # self.color('white')
        # self.goto(-7, 260)
        # self.write(arg=f"SCORE: {self.count}", move=False, align='center', font=("Helvetica", 24, 'bold'))
        self.update_scoreboard()

    def score_increase(self):
        self.count += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.color('white')
        self.goto(-7, 260)
        self.write(arg=f"SCORE: {self.count}", move=False, align='center', font=("Helvetica", 24, 'bold'))

        self.color('grey')
        self.goto(150, 260)
        self.write(arg=f"High Score: {self.highscore}", move=False, align='left', font=("Courier", 12, 'bold'))

    # def game_over(self):
    #     self.color('grey')
    #     self.speed(0)
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", move=False, align='center', font=("Courier", 20, 'bold'))

    def high_score(self):
        self.highscore = max(self.highscore, self.count)
        with open("savedHighScore.txt", mode='w') as file:
            file.write(str(self.highscore))
        self.count = 0
        self.update_scoreboard()
