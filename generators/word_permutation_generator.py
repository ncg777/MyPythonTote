from generators.combination_generator import CombinationGenerator
from generators.mixed_radix_generator import MixedRadixGenerator

class WordPermutationGenerator:
    """
    Generates the combinatorial objects associated with multinomial coefficients
    in reverse lexicographic order.
    
    For example, to enumerate the permutations of MISSISSIPPI, 
   
    rk would be {1,4,4,2} because it has 1 M, 4 Is, 4 Ss, and 2 Ps.
   
    In the enumerated arrays, the 0s represent the M, the 1s the I,
    the 2s the S and the 3 the Ps.
    """
    def __init__(self, rk):
        if rk is None:
            raise RuntimeError("null array")
        
        k = len(rk)
        self.n = 0

        self.nonzeroindices = []
        for i in range(k):
            if rk[i] < 0:
                raise RuntimeError("null or negative element")
            self.n += rk[i]
            if rk[i] != 0:
                self.nonzeroindices.append(i)

        self.combis = []
        sizes = []
        c = 0
        for i in range(len(self.nonzeroindices)):
            nz = self.nonzeroindices[i]
            c += rk[nz]
            self.combis.append(list(CombinationGenerator(c, rk[nz])))
            sizes.append(len(self.combis[i]))

        self.it = MixedRadixGenerator(sizes)

    def __iter__(self):
        return self

    def __next__(self):
        mr = next(self.it)
        pos = list(range(self.n))
        x = [0] * self.n

        for i in range(len(mr) - 1, -1, -1):
            p = self.combis[i][mr[i]]
            for j in range(p.n - 1, -1, -1):
                if p.get(j):
                    x[pos[j]] = self.nonzeroindices[i]
                    del pos[j]

        return x