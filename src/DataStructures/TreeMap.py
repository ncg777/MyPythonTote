from sortedcontainers import SortedDict

class TreeMap(SortedDict):
    def __init__(self):
        super(TreeMap, self).__init__()

    def put(self, key, value):
        self[key] = value

    def get(self, key):
        return self[key]

    def containsKey(self, key):
        return key in self

    def containsValue(self, value):
        for k, v in self.entrySet():
            if v == value:
                return True
        return False

    def size(self):
        return len(self)

    def isEmpty(self):
        return len(self) == 0

    def remove(self, key):
        del self[key]

    def keySet(self):
        return set(self.keys())

    def values(self):
        return list(self.values())

    def entrySet(self):
        return list(self.items())

    def firstKey(self):
        return min(self.keys())

    def lastKey(self):
        return max(self.keys())

    def floorKey(self, key):
        return max(x for x in self.keys() if x <= key)

    def ceilingKey(self, key):
        try:
            return min(x for x in self.keys() if x >= key)
        except ValueError:
            return None
    def lowerKey(self, key):
        try:
            return max(x for x in self.keys() if x < key)
        except ValueError:
            return None

    def higherKey(self, key):
        try:
            return min(x for x in self.keys() if x > key)
        except ValueError:
            return None

    def pollFirstEntry(self):
        if not self:
            return None
        key = min(self.keys())
        value = self[key]
        del self[key]
        return key, value

    def pollLastEntry(self):
        if not self:
            return None
        key = max(self.keys())
        value = self[key]
        del self[key]
        return key, value
    
    def copyOf(self):
        return TreeMap(self)

    def comparator(self):
        return self._SortedDict__cmp

    def entrySet(self):
        return list(self.items())

    def keySet(self):
        return set(self.keys())

    def values(self):
        return [v for k, v in self.entrySet()]

    def putAll(self, map):
        self.update(map)

    def subMap(self, fromKey, fromInclusive, toKey, toInclusive):
        return {k: self[k] for k in self.keys() if (fromInclusive and k >= fromKey) and (toInclusive and k <= toKey)}

    def headMap(self, toKey, inclusive):
        return {k: self[k] for k in self.keys() if k < toKey or (inclusive and k == toKey)}

    def tailMap(self, fromKey, inclusive):
        return {k: self[k] for k in self.keys() if k > fromKey or (inclusive and k == fromKey)}

    def descendingKeySet(self):
        return sorted(self.keys(), reverse=True)

    def descendingMap(self):
        return {k: self[k] for k in sorted(self.keys(), reverse=True)}

    def navigateableKeySet(self):
        return sorted(self.keys())

    def navigateableEntrySet(self):
        return sorted(self.items())

    def pollLastEntry(self):
        if not self:
            return None
        key = max(self.keys())
        value = self[key]
        del self[key]
        return key, value

    def replace(self, key, value):
        if key in self:
            self[key] = value

    def replace(self, key, oldValue, newValue):
        if key in self and self[key] == oldValue:
            self[key] = newValue