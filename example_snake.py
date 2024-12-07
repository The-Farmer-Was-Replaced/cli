from src.snake import Snake

# Create a new instance of the game.
tfwr = Snake() # Create a new instance of the game.

# Play the game manually by typing commands in the terminal.
tfwr.play() # Play the game manually by typing commands in the terminal.



# Or, you can use the following commands to play the game programmatically.

# Movements
# return False if the player hits the wall or itself.
tfwr.move("North") # Move the player up.
tfwr.move("East") # Move the player right.
tfwr.move("South") # Move the player down.
tfwr.move("West") # Move the player left.

# Measure
# return the position of the next apple.
tfwr.measure("North") # Measure the tile above the player.
tfwr.measure("East") # Measure the tile to the right of the player.
tfwr.measure("South") # Measure the tile below the player.
tfwr.measure("West") # Measure the tile to the left of the player.
tfwr.measure() # Measure the tile the player is on.

# Clear
# Returns the length of the snake and resets the game.
tfwr.clear() # Clear the game.
