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
    
    def symmetricDifference(self, other):
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
    
    def iter_search(self, value):
        for i in range(self.n):
            if self.get(i) == value:
                yield i

    def toBinaryString(self):
        return self.toString()

    def __str__(self):
        output = ', '.join(str(i) for i in self.iter_search(1))
        if output:
            output = '{' + output + '}'
        return output

    def asSequence(self):
        return [i for i in self.iter_search(1)]

    def asBinarySequence(self):
        return [1 if self.get(i)==True else 0 for i in range(self.n)]

    @staticmethod
    def fromBinarySequence(s):
        c = data_structures.combination.Combination(len(s))
        for i, v in enumerate(s):
            if v:
                c.set(i)
        return c

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