import data_structures
import data_structures.combination

class Composition(data_structures.combination.Combination):
    def __init__(self, n):
        super().__init__(n - 1)

    @staticmethod
    def from_combination(c):
        nsb = c.next_set_bit(0)
        if nsb == -1:
            raise ValueError("Combination has 0 cardinality")
        t = c.rotate(-nsb)
        o = Composition(t.n)
        for i in range(1, t.n, 1):
            o[i-1]=t[i]
        return o

    @staticmethod
    def from_array(a):
        s = sum(a)
        c = data_structures.combination.Combination(s)
        acc = 0
        for i,v in enumerate(a):
            c.set(acc)
            acc += v
        return Composition.from_combination(c)

    def get_total(self):
        return self.n + 1

    def to_array(self):
        o = []
        x = 1
        for i in range(self.n):
            if self[i]:
                o.append(x)
                x = 1
            else:
                x += 1
        o.append(x)
        return o
    
    def __str__(self):
        output = ', '.join(str(i) for i in self.to_array())
        if output:
            output = '[' + output + ']'
        return output
    
    def to_combination(self):
        o = data_structures.combination.Combination(self.n + 1)
        o.set(0)
        for i in range(1, self.n + 1):
            o.set(i, self.get(i - 1))
        return o