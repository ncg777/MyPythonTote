import DataStructures.Combination
class CombinationGenerator:
    def __init__(self, n, k):
        self.current = self.first(n, k)

    @staticmethod
    def first(n, k):
        o = DataStructures.Combination.Combination(n)
        for i in range(k):
            o.set(i, True)
        return o

    @staticmethod
    def next(c):
        n = c.getN()
        o = None
        j = -1
        for i in range(n - 1):
            if c.get(i) and not c.get(i + 1):
                j = i
                break
        if j != -1:
            o = DataStructures.Combination.Combination(c)
            o.set(j, False)
            o.set(j + 1, True)
            s = -1
            for i in range(j):
                if not o.get(i):
                    s = i
                    break
            for i in range(j, -1, -1):
                if o.get(i) and s != -1 and s < i:
                    o.set(i, False)
                    o.set(s, True)
                    while s < j and o.get(s):
                        s += 1
        return o

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        o = self.current
        self.current = self.next(self.current)
        return o