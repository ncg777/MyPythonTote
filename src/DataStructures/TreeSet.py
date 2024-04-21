from sortedcontainers import SortedSet

class TreeSet(SortedSet):
    def add(self, elem):
        SortedSet.add(self, elem)

    def remove(self, elem):
        if elem in self:
            SortedSet.remove(self, elem)

    def contains(self, elem):
        return elem in self

    def size(self):
        return len(self)

    def isEmpty(self):
        return len(self) == 0

    def iterator(self):
        return iter(self)

    def descendingIterator(self):
        return iter(reversed(self))

    def subSet(self, fromElement, fromInclusive, toElement, toInclusive):
        return TreeSet(e for e in self if (fromInclusive and e >= fromElement) and (toInclusive and e <= toElement))

    def headSet(self, toElement, inclusive):
        return TreeSet(e for e in self if e < toElement or (inclusive and e == toElement))

    def tailSet(self, fromElement, inclusive):
        return TreeSet(e for e in self if e > fromElement or (inclusive and e == fromElement))

    def first(self):
        return min(self)

    def last(self):
        return max(self)

    def lower(self, e):
        return max(x for x in self if x < e)

    def floor(self, e):
        return max(x for x in self if x <= e)

    def ceiling(self, e):
        return min(x for x in self if x >= e)

    def higher(self, e):
        return min(x for x in self if x > e)

    def pollFirst(self):
        return self.pop(0)

    def pollLast(self):
        return self.pop()
    
    def copyOf(self):
        return TreeSet(self)