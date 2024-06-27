import turtle as t

SNAKE_STARTING_CORD = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.current_speed = 6
        self.snake_creation()
        self.snake_head = self.snake_body[0]

    def snake_creation(self):
        for position in SNAKE_STARTING_CORD:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle(shape='circle')
        new_segment.penup()
        new_segment.speed(self.current_speed)
        new_segment.color('white')
        new_segment.goto(position)
        self.snake_body.append(new_segment)

    def extension(self):
        self.add_segment(self.snake_body[-1].position())
        # self.add_segment(len(self.snake_body))  # Not very effective.

    def reset(self):
        for snake in self.snake_body:
            snake.goto(2000, 2000)
        self.snake_body.clear()
        self.snake_body = []
        self.snake_creation()
        self.snake_head = self.snake_body[0]  # Have to reassign the snake head if not snake wouldn't move.

    def move(self):
        # To move the snake forward, each segment has to move to the position of the segment in front of it.
        # Note: Segments are arranged and added from right to left.
        for segment_number in range(len(self.snake_body) - 1, 0, -1):  # in descending order(starting from the end)
            updated_x_cord = self.snake_body[segment_number - 1].xcor()  # x coordinate of the immediate prior segment.
            updated_y_cord = self.snake_body[segment_number - 1].ycor()  # y coordinate of the immediate prior segment.

            self.snake_body[segment_number].goto(updated_x_cord, updated_y_cord)

        self.snake_body[0].forward(MOVE_DISTANCE)
        # self.snake_body[0].left(90)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)
