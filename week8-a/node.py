from collections import namedtuple

Item = namedtuple("Item", ['index', 'value', 'weight'])

class Node:
    def __init__(self, index, taken, value, room):
        self.value = value
        self.room = room
        self.index = index
        self.taken = taken
        self.bound = 0
        return

    def estimate(self, items):
        if self.room <= 0:
            self.bound = self.value
            return self.bound
        
        total_val = self.value

        for i in range(self.index, len(items)):
            item = items[i]
            total_val += item.value
           
        self.bound = total_val
        return self.bound
