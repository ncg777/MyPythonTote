from typing import Dict, List, Tuple, Callable
from collections import deque
import data_structures.collection_utils as collection_utils
import data_structures
import data_structures.treemap
import data_structures.treeset

class Sequence:
    def __init__(self, p_arr: List[int] = None):
        self.data = p_arr if p_arr is not None else []

    def to_array(self):
        return self.data.copy()
    
    def calc_interval_vector(self) -> Dict[int, List[int]]:
        return collection_utils.calc_interval_vector_int(self.data)

    def contains(self, n):
        return n in self.data

    def antidifference(self, k: int) -> List[int]:
        return Sequence(collection_utils.antidifference(self.data, k))

    def difference(self) -> List[int]:
        return Sequence(collection_utils.difference(self.data))

    def cyclical_difference(self) -> List[int]:
        return Sequence(collection_utils.cyclical_difference(self))

    def cyclical_antidifference(self, k: int) -> List[int]:
        return Sequence(collection_utils.cyclical_antidifference(self.data, k))

    def reversed(self):
        return Sequence(list(reversed(self)))
    
    def get(self, index: int) -> int:
        return self.data[index]

    def size(self) -> int:
        return len(self.data)

    def add(self, value: int) -> None:
        self.data.append(value)

    def set(self, index: int, value: int) -> None:
        self.data[index] = value

    def distinct(self) -> set:
        return set(self.data)

    def count(self, n: int) -> int:
        return self.data.count(n)

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_std_dev(self) -> float:
        mean = self.get_mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance ** 0.5

    def rotate(self, n: int) -> 'Sequence':
        l = len(self.data)
        n2 = n
        while n2 < 0:
            n2 += l
        while n2 > l:
            n2 -= l
        o = []
        for i,v in enumerate(self.data):
            o.append(self.data[(l+i-n2)%l])
        return Sequence(o)

    def map_ordinals_unipolar(self):
        o = data_structures.treemap.TreeMap();
        d =  self.distinct();
        k = 0
        for i,v in enumerate(d):
            o.put(v, k);
            k += 1
        return o;

    def to_ordinals_unipolar(self):
        return self.map_with_dict(self.map_ordinals_unipolar())

    def map_ordinals_bipolar(self):
        o = data_structures.treemap.TreeMap()
        o.put(0, 0);
        d =  self.distinct();
        abs_d = data_structures.treeset.TreeSet();
        for i,v in enumerate(d):
            abs_d.add(abs(v))
            abs_d.remove(0);
            k = 1;
        for i,v in enumerate(abs_d):
            o.put(v, k);
            o.put(-v, -k);
            k +=1
        return o
    
    def to_ordinals_bipolar(self):
        return self.map_with_dict(self.map_ordinals_bipolar())
  
    def map_with_dict(self, mapping: dict) -> 'Sequence':
        return Sequence([mapping.get(x) for x in self.data])

    def permutate(self, s: 'Sequence') -> 'Sequence':
        return Sequence([self.data[s.get(i)] for i in range(s.size())])

    def juxtapose(self, s: 'Sequence') -> 'Sequence':
        return Sequence(self.data + s.data)

    def get_period(self) -> int:
        for i in range(1, self.size()):
            if self == self.rotate(i):
                return i
        return self.size()

    def circular_hold_non_zero(self) -> 'Sequence':
        last_non_zero = next((i for i in range(self.size() - 1, -1, -1) if self.get(i) != 0), -1)
        if last_non_zero == -1:
            return Sequence([1] * self.size())
        result = Sequence(self.data)
        for i in range(self.size()):
            if result.get(i) == 0:
                k = 1
                while result.get((i - k + self.size()) % self.size()) == 0:
                    k += 1
                v = result.get((i - k + self.size()) % self.size())
                for j in range(k):
                    result.set((i - j + self.size()) % self.size(), v)
        return result

    def __eq__(self, other: 'Sequence') -> bool:
        return self.data == other.data

    def __str__(self) -> str:
        return ' '.join(map(str, self.data))

    def __repr__(self) -> str:
        return f'Sequence({self.data})'

    def __add__(self, n: 'int') -> 'Sequence':
        return Sequence([x + n for x in self.data])

    def __add__(self, other: 'Sequence') -> 'Sequence':
        return self.juxtapose(other)

    def __mul__(self, other: int) -> 'Sequence':
        return Sequence([x * other for x in self.data])

    def __len__(self) -> int:
        return self.size()

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.set(index, value)