from src.cactus import Cactus

tfwr = Cactus()

def move(direction):
    return tfwr.move(direction)

def measure(direction=None):
    return tfwr.measure(direction)

def swap(direction):
    return tfwr.swap(direction)

def clear():
    return tfwr.clear()

def replant():
    return tfwr.replant()

def get_tick_count():
    return tfwr.get_tick_count()

def simple_sort(self):
    if tfwr.measure('West') > tfwr.measure():
        tfwr.swap('West')
    if tfwr.measure('North') < tfwr.measure():
        tfwr.swap('North')
    if tfwr.measure('South') > tfwr.measure():
        tfwr.swap('South')
    if tfwr.measure('East') < tfwr.measure():
        tfwr.swap('East')
    if tfwr.measure('West') > tfwr.measure():
        tfwr.swap('West')
    if tfwr.measure('North') < tfwr.measure():
        tfwr.swap('North')
    if tfwr.measure('South') > tfwr.measure():
        tfwr.swap('South')
    if tfwr.measure('East') < tfwr.measure():
        tfwr.swap('East')

path = [
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
    "North", "North", "North", "North", "North", "North", "North", "North", "North", "East",
]

timings = []
for _ in range(1000):
    ticks = get_tick_count()
    for _ in range(6):
        for direction in path:
            move(direction)
            simple_sort(tfwr)
    if clear():
        timings.append(get_tick_count() - ticks)

print("min:", min(timings), "max:", max(timings), "avg:", sum(timings) / len(timings))
# min: 277200 max: 322600 avg: 298106.62323561346
