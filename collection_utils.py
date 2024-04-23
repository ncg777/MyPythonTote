import random
import data_structures
from typing import Collection, Iterator, List, Set, Dict, Any


def filter_set(s: Set[Any], p: Any) -> None:
    x = [a for a in s if p(a)]
    s.intersection_update(x)

def choose_at_random(i: Iterator[Any], n: int) -> Any:
    if i is None or n <= 0:
        raise RuntimeError("Invalid arguments")
    o = None
    k = 0
    r = random.randint(0, n-1)
    while k <= r:
        o = next(i)
        k += 1
    return o

def choose_at_random_with_weights(i: Iterator[Any], n: int, weights: List[float]) -> Any:
    if i is None or n <= 0 or weights is None or len(weights) != n:
        raise RuntimeError("Invalid arguments")
    normalized_weights = [weights[j]/sum(weights) for j in range(n)]
    acc = 0.0
    o = None
    k = 0
    r = random.random()
    while True:
        o = next(i)
        acc += normalized_weights[k]
        if r <= acc:
            break
        k += 1
    return o

def choose_at_random(t: Collection[Any]) -> Any:
    return choose_at_random(t.__iter__(), len(t))

def choose_at_random_with_weights(t: Collection[Any], weights: List[float]) -> Any:
    return choose_at_random_with_weights(t.__iter__(), len(t), weights)

def map_is_bijective(m: Dict[Any, Any]) -> bool:
    return len(m.keys()) == len(set(m.values()))

def rotate(arr: List[Any], n: int) -> List[Any]:
    c = arr.copy()
    m = n
    while m < 0:
        m += len(c)
    while m > len(c):
        m -= len(c)
    for i in range(len(c)):
        c[i] = arr[(i + len(c) - m) % len(c)]
    return c

def map_using_permutation(s: List[int], p: List[int]) -> List[int]:
    i = data_structures.treemap.TreeMap()
    for x in range(len(p)):
        i[x] = p[x]
    return map_with_dict(s, i)

def invert_map(map: Dict[Any, Any]) -> Dict[Any, Any]:
    if not map_is_bijective(map):
        raise RuntimeError("The map is not bijective; it cannot be inverted.")
    o = data_structures.treemap.TreeMap()
    for k, v in map.items():
        o[v] = k
    return o

def map_with_dict(s: List[int], i: Dict[int, int]) -> List[int]:
    output = [0] * len(s)
    for x in range(len(s)):
        output[x] = i.get(s[x], s[x])
    return output

def size_of_codomain(s: List[int]) -> int:
    t = set(s)
    return len(t)

def calc_interval_vector_bool(input: List[bool]) -> List[int]:
    n = len(input)
    m = n // 2
    s = []
    for i in range(1,m+1,1):
      k = 0;
      for j in range(n):
        if input[j] and input[(i + j) % n]:
          k += 1
      if i == m and n % 2 == 0:
        k = k / 2;
      s.append(k);
    return s;

def calc_interval_vector_int(input: List[int]) -> Dict[int, List[int]]:
    output = {}
    t = set(input)
    for v in t:
        b = [x == v for x in input]
        output[v] = calc_interval_vector_bool(b)
    return output

def antidifference(p_arr: List[int], k: int) -> List[int]:
    output = [0] * (len(p_arr) + 1)
    output[0] = k
    for i in range(len(p_arr)):
        output[i + 1] = output[i] + p_arr[i]
    return output

def difference(p_arr: List[int]) -> List[int]:
    output = [0] * (len(p_arr) - 1)
    for i in range(1, len(p_arr)):
        output[i - 1] = p_arr[i] - p_arr[i - 1]
    return output

def cyclical_difference(p_arr: List[int]) -> List[int]:
    output = [0] * len(p_arr)
    for i in range(len(p_arr)):
        output[(i+1)%len(p_arr)] = p_arr[(i + 1)%len(p_arr)] - p_arr[i]
    return output

def cyclical_antidifference(p_arr: List[int], k: int) -> List[int]:
    output = [0] * len(p_arr)
    output[len(p_arr)-1] = k
    for i in range(len(p_arr)):
        output[i] = output[(i-1 + len(p_arr))%len(p_arr)] + p_arr[(i-1 + len(p_arr))%len(p_arr)]
    return output

def random_permutation(n: int) -> List[int]:
    o = []
    t = set(range(n))
    for i in range(n):
        j = choose_at_random(t)
        t.remove(j)
        o.append(j)
    return o

def permutate(p: List[int], arr: List[Any]) -> List[Any]:
    n = len(arr)
    o = []
    for i in range(n):
        o.append(arr[p[i]])
    return o

def permutate_randomly(arr: List[Any]) -> List[Any]:
    return permutate(random_permutation(len(arr)), arr)