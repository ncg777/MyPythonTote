class MixedRadixGenerator:
    """
    Enumerates all values of the mixed radix base given as parameter.
    http://en.wikipedia.org/wiki/Mixed_radix

    You could also see it as a cartesian product.
    https://en.wikipedia.org/wiki/Cartesian_product
    
    This Python code was translated by meta.ai within 3 chat interactions from a Java enumeration
    """
    def __init__(self, base):
        self.base = base
        self.current = [0] * len(base)
        self.is_last = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_last:
            raise StopIteration

        result = self.current.copy()
        for i in range(len(self.base) - 1, -1, -1):
            if self.current[i] < self.base[i] - 1:
                self.current[i] += 1
                break
            else:
                self.current[i] = 0
        else:
            self.is_last = True
        return result
