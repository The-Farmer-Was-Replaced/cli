from src.snake import Snake

tfwr = Snake()

def move(direction):
    return tfwr.move(direction)

def measure(direction=None):
    return tfwr.measure(direction)

def clear():
    return tfwr.clear()

def get_tick_count():
    return tfwr.get_tick_count()

path = [
    "North","North","North","North","North","North","North","North","North","East",
    "East","East","East","East","East","East","East","East","South","West","West",
    "West","West","West","West","West","West","South","East","East","East","East",
    "East","East","East","East","South","West","West","West","West","West","West",
    "West","West","South","East","East","East","East","East","East","East","East",
    "South","West","West","West","West","West","West","West","West","South","East",
    "East","East","East","East","East","East","East","South","West","West","West",
    "West","West","West","West","West","South","East","East","East","East","East",
    "East","East","East","South","West","West","West","West","West","West","West","West","West"
]

timings = []
for _ in range(200):
    ticks = get_tick_count()
    can_move = True
    while can_move:
        for direction in path:
            if not move(direction):
                can_move = False
                break
    if clear():
        timings.append(get_tick_count() - ticks)

print("min:", min(timings), "max:", max(timings), "avg:", sum(timings) / len(timings))
# min: 1774154.0 max: 2310993.0 avg: 2030866.96
