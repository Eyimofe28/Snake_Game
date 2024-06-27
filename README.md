**Overview**

In this project, I implemented the ever classic Snake Game using the turtle graphics library in Python. The game includes key features such as dynamic snake movement, food generation, score tracking, and game resetting upon collision. The project is structured into multiple modules to handle different aspects of the game, ensuring modularity and ease of understanding.

**Project Structure**
```
SnakeGame/
│
├── snake_main.py
├── snake_movement.py
├── snake_food.py
├── scoreboard.py
└── savedHighScore.txt
```

**Files**
1. snake_main.py: The main file that sets up the game environment and runs the game loop.
2. snake_movement.py: Handles the snake's creation, movement, and extension.
3. snake_food.py: Manages the creation and movement of the food object.
4. scoreboard.py: Tracks and displays the score and high score.
5. savedHighScore.txt: Stores the high score between game sessions.

**Dependencies**
- Python 3.x
- turtle module (standard library)
- time module (standard library)
- random module (standard library)

**Setup and Execution**
1. Clone the Repository:
   ```bash
   git clone https://github.com/yourusername/SnakeGame.git
   cd SnakeGame
   ```

2. Run the Game:
   ```bash
   python snake_main.py
   ```
