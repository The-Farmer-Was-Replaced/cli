import random

class Game:
    def __init__(self, seed=None):
        random.seed(seed)
        self.world_size = 10
        self.player_pos = [0, 0]
        self.ticks = 0
        self.grid = self.create_grid()

    def create_grid(self):
        return [["░░░" for y in range(self.world_size)] for x in range(self.world_size)]

    def get_tick_count(self):
        return self.ticks

    def get_pos_x(self):
        return self.player_pos[0]

    def get_pos_y(self):
        return self.player_pos[1]

    def display_grid(self):
        for y in range(self.world_size - 1, -1, -1):
            line = ''
            for x in range(self.world_size):
                if [x, y] == self.player_pos:
                    if self.grid[x][y].startswith("🌻") and len(self.grid[x][y]) == 3:
                        line += f'[{self.grid[x][y]}'
                    else:
                        line += f'[{self.grid[x][y]}]'
                else:
                    line += f' {self.grid[x][y]} '
            print(line, end='\n\n')

    def clear(self):
        self.grid = self.create_grid()
        self.player_pos = [0, 0]

    def move(self, direction):
        self.ticks += 200
        match direction:
            case 'w' | 'North':
                self.player_pos[1] = (self.player_pos[1] + 1) % self.world_size
            case 's' | 'South':
                self.player_pos[1] = (self.player_pos[1] - 1) % self.world_size
            case 'a' | 'West':
                self.player_pos[0] = (self.player_pos[0] - 1) % self.world_size
            case 'd' | 'East':
                self.player_pos[0] = (self.player_pos[0] + 1) % self.world_size
            case _:
                raise ValueError("Invalid move direction.", direction)

    def swap(self, direction):
        tx, ty = self.player_pos[0], self.player_pos[1]
        self.ticks += 200
        match direction:
            case 'North':
                ty += 1
            case 'South':
                ty -= 1
            case 'West':
                tx -= 1
            case 'East':
                tx += 1
            case _:
                raise ValueError("Invalid swap direction.", direction)

        if 0 <= tx < self.world_size and 0 <= ty < self.world_size:
            self.grid[self.player_pos[0]][self.player_pos[1]], self.grid[tx][ty] = \
                self.grid[tx][ty], self.grid[self.player_pos[0]][self.player_pos[1]]
            return True
        return False


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
        digits = ''.join(c for c in self.grid[x][y] if c.isdigit())
        return int(digits) if digits else None


    def plant(self, entity):
        self.ticks += 200
        x, y = self.player_pos
        match entity:
            case 'cactus':
                self.grid[x][y] = "🌵" + str(random.randint(0, 9))
            case 'sunflower':
                self.grid[x][y] = "🌻" + str(random.randint(7, 15))
            case 'tree':
                self.grid[x][y] = "🌳 "
            case 'bush':
                self.grid[x][y] = "🌿 "
            case 'grass':
                self.grid[x][y] = "🌱 "

    def replant(self):
        self.ticks += 200 * 3
        match self.grid[self.player_pos[0]][self.player_pos[1]][0]:
            case '🌵':
                self.grid[self.player_pos[0]][self.player_pos[1]] = "🌵" + str(random.randint(0, 9))
            case '🌻':
                self.grid[self.player_pos[0]][self.player_pos[1]] = "🌻" + str(random.randint(7, 15))
            case '🌳':
                self.grid[self.player_pos[0]][self.player_pos[1]] = "🌳 "
            case '🌿':
                self.grid[self.player_pos[0]][self.player_pos[1]] = "🌿 "
            case '🌱':
                self.grid[self.player_pos[0]][self.player_pos[1]] = "🌱 "
            case _:
                raise ValueError("Invalid entity.", self.grid[self.player_pos[0]][self.player_pos[1]])

    def play(self):
        while True:
            self.display_grid()
            cmd = input("")
            print("\033[H\033[J")

            cmd0 = cmd.split()[0] if len(cmd.split()) > 0 else None

            match cmd0:
                case None:
                    pass

                case 'q':
                    break

                case 'w' | 's' | 'a' | 'd':
                    self.move(cmd0)

                case 'move':
                    direction = cmd.split()[1] if len(cmd.split()) > 1 else None
                    self.move(direction)

                case 'swap':
                    direction = cmd.split()[1] if len(cmd.split()) > 1 else None
                    self.swap(direction)

                case 'measure':
                    direction = cmd.split()[1] if len(cmd.split()) > 1 else None
                    print("Measured: ", str(self.measure(direction)))

                case 'plant':
                    entity = cmd.split()[1] if len(cmd.split()) > 1 else None
                    self.plant(entity)

                case 'replant':
                    self.replant()

                case 'clear':
                    self.clear()

                case _:
                    print("Invalid command.")


if __name__ == '__main__':
    game = Game()
    # game.play()
    game.plant("tree")
    game.move("North")
    game.plant("cactus")
    game.display_grid()
