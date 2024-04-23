import data_structures
from generators.combination_generator import CombinationGenerator

class Combination(data_structures.bitset.BitSet):
    def __init__(self, n):
        super().__init__(n)

    def compare(self, other):
        if not isinstance(other, Combination):
            raise ValueError("Can only compare with another Combination")
        if self.n != other.n:
            raise ValueError("Combinations must be of the same size")
        for i in range(self.n):
            if self.get(i) != other.get(i):
                return self.get(i) - other.get(i)
        return 0
    
    def symmetric_difference(self, other):
        if not isinstance(other, Combination):
            raise ValueError("Can only perform symmetric difference with another Combination")
        if self.n != other.n:
            raise ValueError("Combinations must be of the same size")
        result = Combination(self.n)
        for i in range(self.n):
            result.set(i, (self.get(i) != other.get(i)))
        return result

    def __eq__(self, other):
        return self.compare(other) == 0

    def __hash__(self):
        return hash((super().__hash__(), self.n))

    def __str__(self):
        output = ', '.join(str(i) for i in self.iter_search(1))
        if output:
            output = '{' + output + '}'
        return output
    
    @staticmethod
    def from_bitset(bs):
        c = Combination(bs.n)
        c.bits = bs.bits
        return c

    @staticmethod
    def from_binary_array(a):
        b = data_structures.bitset.BitSet.from_binary_array(a)
        return Combination.from_bitset(b)
    
    @staticmethod
    def from_bitstring(bs):
        b = data_structures.bitset.BitSet.from_bitstring(bs)        
        return Combination.from_bitset(b);

    def rotate(self, t):
        k = t
        while k < 0:
            k += self.n
        while k >= self.n:
            k -= self.n
        x = data_structures.bitset.BitSet(self.n)
        for i in range(self.n):
            x[i] = self[(i - k + self.n) % self.n]
        o = Combination(self.n)
        o.or_(x)
        return o
    
    def union(self, other):
        result = Combination(self.n)
        for i in range(self.n):
            result.set(i, self.get(i) or other.get(i))
        return result

    def intersection(self, other):
        result = Combination(self.n)
        for i in range(self.n):
            result.set(i, self.get(i) and other.get(i))
        return result

    def minus(self, other):
        result = Combination(self.n)
        for i in range(self.n):
            result.set(i, self.get(i) and not other.get(i))
        return result
        
    def __hash__(self):
        return hash(tuple(self.bits))