import DataStructures

class Composition(DataStructures.Combination.Combination):
    def __init__(self, n):
        super().__init__(n - 1)

    def getTotal(self):
        return self.n + 1

    def asList(self):
        o = []
        n = 1
        for i in range(self.m_n):
            if self.get(i):
                o.append(n)
                n = 1
            else:
                n += 1
        o.append(n)
        return o

    def asCombination(self):
        o = DataStructures.Combination.Combination(self.m_n + 1)
        o.set(0)
        for i in range(1, self.m_n + 1):
            o.set(i, self.get(i - 1))
        return o

    def degrade(self):
        c = self.cardinality()
        if c == 0:
            return DataStructures.Composition.Composition()
        o = DataStructures.Composition.Composition(self.getTotal() - 1)
        if c == 1:
            return o
        i = self.next_set_bit(0)
        for j in range(o.m_n):
            o.set(j, self.get((j + i + 1) % o.m_n))
        return o

    def partitionByEquality(self):
        s = self.asList()
        groups = [0] * len(s)
        k = 0
        for j in range(len(s) - 1, -1, -1):
            if s[0] == s[j]:
                k -= 1
            else:
                break
        k += len(s)
        k %= len(s)
        previousValue = s[k]
        currentGroup = 0
        for i in range(k + 1, len(s) + k):
            v = s[i % len(s)]
            if v != previousValue:
                currentGroup += 1
            groups[i % len(groups)] = currentGroup
            previousValue = v
        return groups