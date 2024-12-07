import random
import src.game as game

class Cactus(game.Game):
    def __init__(self, seed=None):
        super().__init__(seed)
        self.clear()

    def create_grid(self):
        return [["🌵" + str(random.randint(0, 9)) for y in range(self.world_size)] for x in range(self.world_size)]

    def plant(self, entity):
        raise NotImplementedError("Snake does not support plant.")

    def replant(self):
        self.ticks += 200 * 3
        self.grid[self.player_pos[0]][self.player_pos[1]] = "🌵" + str(random.randint(0, 9))

    def clear(self):
        sorted = self._is_sorted()
        super().clear()
        return sorted

    def _is_sorted(self):
        wrong_positions = []
        for y in range(self.world_size - 1, -1, -1):
            for x in range(self.world_size):
                current = self.grid[x][y]
                # Check North neighbor
                if y < self.world_size - 1 and self.grid[x][y + 1] < current:
                    wrong_positions.append([x, y])
                # Check East neighbor
                if x < self.world_size - 1 and self.grid[x + 1][y] < current:
                    wrong_positions.append([x, y])
                # Check South neighbor
                if y > 0 and self.grid[x][y - 1] > current:
                    wrong_positions.append([x, y])
                # Check West neighbor
                if x > 0 and self.grid[x - 1][y] > current:
                    wrong_positions.append([x, y])
        return len(wrong_positions) == 0
