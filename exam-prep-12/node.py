from collections import namedtuple


Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.index = index
        self.taken = taken
        self.value = value
        self.room  = room

    def estimate(self, items):
        return self.value + sum(item.value for item in items[self.index:])