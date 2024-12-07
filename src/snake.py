import random
import src.game as game

class Snake(game.Game):
    def __init__(self, seed=None):
        super().__init__(seed)
        self._length = 0
        self._snake_body = []
        self._apple_spawn_pos = self._get_empty_tile()
        self.grid[self.player_pos[0]][self.player_pos[1]] = '🍎 '

    def clear(self):
        score = self._length
        self.grid = self.create_grid()
        self.player_pos = [0, 0]
        self._length = 0
        self._snake_body = []
        self._apple_spawn_pos = self._get_empty_tile()
        self.grid[self.player_pos[0]][self.player_pos[1]] = '🍎 '
        return score

    def display_grid(self):
        for y in range(self.world_size - 1, -1, -1):
            line = ''
            for x in range(self.world_size):
                if [x, y] == self.player_pos:
                    if self.grid[self.player_pos[0]][self.player_pos[1]] == '🍎 ':
                        line += f'🐔🍎 '
                    else:
                        line += f' 🐔  '
                else:
                    line += f' {self.grid[x][y]} '
            print(line, end='\n\n')

    def move(self, direction):
        self.ticks += 800 * (self._length * 0.03) // 1
        old_pos = self.player_pos.copy()
        if self._length > 2:
            body = self._snake_body[1:]
        else:
            body = self._snake_body
        match direction:
            case 'w' | 'North':
                if (self.player_pos[0], self.player_pos[1] + 1) in body:
                    return False
                if self.player_pos[1] == self.world_size - 1:
                    return False
                self.player_pos[1] = (self.player_pos[1] + 1)
            case 's' | 'South':
                if (self.player_pos[0], self.player_pos[1] - 1) in body:
                    return False
                if self.player_pos[1] == 0:
                    return False
                self.player_pos[1] = (self.player_pos[1] - 1)
            case 'a' | 'West':
                if (self.player_pos[0] - 1, self.player_pos[1]) in body:
                    return False
                if self.player_pos[0] == 0:
                    return False
                self.player_pos[0] = (self.player_pos[0] - 1)
            case 'd' | 'East':
                if (self.player_pos[0] + 1, self.player_pos[1]) in body:
                    return False
                if self.player_pos[0] == self.world_size - 1:
                    return False
                self.player_pos[0] = (self.player_pos[0] + 1)
            case _:
                raise ValueError("Invalid move direction.", direction)

        if self.grid[old_pos[0]][old_pos[1]] == '🍎 ':
            self._length += 1
            self._snake_body.append((old_pos[0], old_pos[1]))
            self.grid[old_pos[0]][old_pos[1]] = '░o░'
            if self._apple_spawn_pos:
                self.grid[self._apple_spawn_pos[0]][self._apple_spawn_pos[1]] = '🍎 '
        else:
            self._snake_body.append((old_pos[0], old_pos[1]))
            self.grid[old_pos[0]][old_pos[1]] = '░o░'
            self.grid[self._snake_body[0][0]][self._snake_body[0][1]] = '░░░'
            self._snake_body.pop(0)

        if self.grid[self.player_pos[0]][self.player_pos[1]] == '🍎 ':
            self._apple_spawn_pos = self._get_empty_tile()

        return True

    def swap(self, direction):
        raise NotImplementedError("Snake does not support swap.")

    def plant(self, entity):
        raise NotImplementedError("Snake does not support plant.")

    def replant(self):
        raise NotImplementedError("Snake does not support replant.")

    def measure(self, direction=None):
        self.ticks += 1
        x, y = self.player_pos
        if direction:
            match direction:
                case 'North':
                    y = (y + 1) % self.world_size
                case 'South':
                    y = (y - 1) % self.world_size
                case 'West':
                    x = (x - 1) % self.world_size
                case 'East':
                    x = (x + 1) % self.world_size
                case _:
                    raise ValueError("Invalid measure direction.", direction)
        if self.grid[x][y] == '🍎 ':
            if self.grid[self._apple_spawn_pos[0]][self._apple_spawn_pos[1]] != '░░░':
                self._apple_spawn_pos = self._get_empty_tile()
            return self._apple_spawn_pos
        return None

    def _get_empty_tile(self):
        empty_tiles = []
        for x in range(self.world_size):
            for y in range(self.world_size):
                if self.grid[x][y] == '░░░':
                    empty_tiles.append((x, y))
        if not empty_tiles:
            return None
        return random.choice(empty_tiles)

    def play(self):
        while True:
            self.display_grid()
            cmd = input("Enter a command (w/s/a/d/measure/clear): ").lower()
            print("\033[H\033[J")
            if cmd == 'measure':
                print(self.measure())
            elif cmd == 'clear':
                self.clear()
            else:
                self.move(cmd)
