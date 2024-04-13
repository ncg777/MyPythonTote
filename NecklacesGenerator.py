
def _subGen(t, p, n, k, array, necklaces):
        if t > n:
            if (n % p) == 0:
                necklaces.append(array[1:].copy())
        else:
            array[t] = array[t - p]
            _subGen(t+1, p, n, k, array, necklaces)
            for j in range(array[t - p] + 1, k):
                array[t] = j
                _subGen(t+1, t, n, k, array, necklaces)

def generate(n, k):
    necklaces = []
    array = [0] * (n+1)
    _subGen(1, 1, n, k, array, necklaces)
    return necklaces