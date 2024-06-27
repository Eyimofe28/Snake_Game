import random
from turtle import Turtle
# Since the food is a singular turtle object, we can inherit all the properties of Turtle
# in the turtle class and work directly with it.


class Food(Turtle):
    def __init__(self):
        super().__init__()  # To access objects & attributes in turtle class.

        # Setting up food qualities.
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # length and width is usually 20. This reduces them to 10.
        self.color("green")
        self.tilt(135)
        self.speed('fastest')
        self.move()

    def move(self):
        # To move food on the screen.
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
