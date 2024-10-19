import random
from bitarray import bitarray
import numpy as np

class BloomFilter:
    def __init__(self, n, p, num_hashes=7):
        # Calculating the parameters
        self.m = int(-(n * np.log(p)) / (np.log(2) ** 2))
        self.k = num_hashes  # Number of hash functions

        # Initializing the bit array
        self.bit_array = bitarray(self.m)
        self.bit_array.setall(0)

        # Prime number greater than the maximum element length (for hash functions)
        self.p = 104729  # Example prime number

        # Generating random coefficients a and b for hash functions
        self.a = [random.randint(1, self.p - 1) for _ in range(self.k)]
        self.b = [random.randint(0, self.p - 1) for _ in range(self.k)]

    def _hash(self, item):
        # Convert item to an integer hash code
        item_hash = sum([ord(char) for char in item])

        # Generate k hashes for the item using the formula from the screenshot
        return [((self.a[i] * item_hash + self.b[i]) % self.p) % self.m for i in range(self.k)]

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

