# Snake_Game
This is a snake game created in python using Turtle Library. This Program only include Snake movement machanism and snake body. The food part of this program is not yet Developed !!!!

main_snake.py : 
  Explanation:
Snake class: This class contains all the attributes and methods related to the snake.

__init__(): Initializes the snake by creating the segments. The snake starts with three segments.
create_snake(): Adds three initial segments at the starting positions.
add_segment(): Adds a new segment to the snake's body.
move(): Moves the snake by shifting each segment to the position of the previous one.
Movement methods (up(), down(), left(), right()): Change the direction of the snake's head while ensuring it cannot move in the opposite direction.
Main game loop: The code you've written already correctly initializes the game, listens for key presses, and continuously updates the screen while moving the snake.

Improvements and features to consider:
Collisions: Currently, the snake won’t stop if it collides with the walls or itself. You can add logic for collision detection.
Food: You can implement food for the snake to "eat" and grow longer.
Score: You can keep track of the score and display it on the screen.
