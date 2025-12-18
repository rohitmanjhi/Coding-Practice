from ast import Or
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        if capacity < 0:
            return ValueError("capacity must be grater than 0")

        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # make this key most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
             # update value and move to MRU
             self.cache[key] = value
             self.cache.move_to_end(key)
        else:
            # if cache is full, remove LRU
            if len(self.cache) == self.capacity:
                self.cache.popitem(last = False) # Remove LRU 
            self.cache[key] = value 

    # helper to see cache state
    def show(self):
        # Right side = Most Recently Used (RMU)
        # Left side = Least Recently Used (LRU)
        print("Cache (LRU → MRU):", list(self.cache.items()))           

# Create LRU Cache with capacity 2
cache = LRUCache(2)

cache.put(1, 1)
cache.show()     # [(1, 1)]

cache.put(2, 2)
cache.show()     # [(1, 1), (2, 2)]

print(cache.get(1))  # 1
cache.show()         # [(2, 2), (1, 1)]

cache.put(3, 3)      # evicts key 2
cache.show()         # [(1, 1), (3, 3)]

print(cache.get(2))  # -1 (not found)

cache.put(4, 4)      # evicts key 1
cache.show()         # [(3, 3), (4, 4)]

print(cache.get(1))  # -1
print(cache.get(3))  # 3
print(cache.get(4))  # 4
