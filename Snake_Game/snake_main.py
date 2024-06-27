import turtle as t
import time
from snake_movement import Snake
from snake_food import Food
from scoreboard import ScoreBoard

# Setting up the game environment
screen = t.Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.tracer(0)
# screen.screensize(600, 550)
screen.title("SNAKE GAME")

# Creating the snake, food, and scoreboard.
snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

# Letting the snake listen for movements
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Flag to check if game is running.
game_on = True

while game_on:
    screen.update()  # This plus tracer allows the snake segments to move as one.
    # It basically updates the screen to display the snake once every segment of the snake has moved.
    time.sleep(0.1)  # Allows us to see the snake's movement because the update function makes it move very fast.

    snake.move()

    # Increasing the speed of the snake as it progresses.
    if scoreBoard.count % 4 == 0 and snake.current_speed > -1:
        for i in snake.snake_body:
            i.speed(snake.current_speed - 1)

    # Increasing the score, moving food to another position, and increasing snake's length when it collides with food.
    if snake.snake_head.distance(food) < 13:
        food.move()
        scoreBoard.score_increase()
        snake.extension()

    # Restarting the game once snake hits wall.
    if (snake.snake_head.xcor() > 290 or snake.snake_head.xcor() < -290 or
            snake.snake_head.ycor() > 290 or snake.snake_head.ycor() < -290):
        # game_on = False
        scoreBoard.high_score()
        snake.reset()
        # scoreBoard.game_over()

    # Restarting the game once snake hits its tail.
    for i in snake.snake_body[1:]:
        if snake.snake_head.distance(i) < 5:
            scoreBoard.high_score()
            snake.reset()
            # game_on = False
            # scoreBoard.game_over()


screen.exitonclick()
