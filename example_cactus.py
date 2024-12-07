from src.cactus import Cactus

# Create a new instance of the game.
tfwr = Cactus() # Create a new instance of the game.

# Play the game manually by typing commands in the terminal.
tfwr.play() # Play the game manually by typing commands in the terminal.



# Or, you can use the following commands to play the game programmatically.

# Movements
tfwr.move("North") # Move the player up.
tfwr.move("East") # Move the player right.
tfwr.move("South") # Move the player down.
tfwr.move("West") # Move the player left.

# Measure
# return the size of the cactus
tfwr.measure("North") # Measure the tile above the player.
tfwr.measure("East") # Measure the tile to the right of the player.
tfwr.measure("South") # Measure the tile below the player.
tfwr.measure("West") # Measure the tile to the left of the player.
tfwr.measure() # Measure the tile the player is on.

# Swap
# Swap the cactus under the player with the cactus in the direction.
tfwr.swap("North") # Swap with the tile above the player.
tfwr.swap("East") # Swap with the tile to the right of the player.
tfwr.swap("South") # Swap with the tile below the player.
tfwr.swap("West") # Swap with the tile to the left of the player.

# Clear
# Returns True if all cacti are sorted correctly.
tfwr.clear() # Clear the game.

# Replant
# Changes the cactus height of the cactus the player is on.
# Equivalent to till(), till(), plant(Entity.Cactus)
tfwr.replant() # Changes the cactus height of the cactus the player is on.
