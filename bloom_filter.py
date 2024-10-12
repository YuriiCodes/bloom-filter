import mmh3
from bitarray import bitarray
import numpy as np

class BloomFilter:
    def __init__(self, n, p):
        # Calculating the parameters
        self.m = int(-(n * np.log(p)) / (np.log(2) ** 2))
        self.k = int((self.m / n) * np.log(2))

        # Initializing the bit array
        self.bit_array = bitarray(self.m)
        self.bit_array.setall(0)
        self.size = n

    def _hash(self, item):
        # Generate k hashes for the item
        return [mmh3.hash(item, i) % self.m for i in range(self.k)]

    def add(self, item):
        # Add the item in the filter
        for h in self._hash(item):
            self.bit_array[h] = 1

    def check(self, item):
        # Check for existence of an item in the filter
        if all(self.bit_array[h] for h in self._hash(item)):
            return "Y"
        else:
            return "N"

