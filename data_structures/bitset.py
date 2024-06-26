import sys

class BitSet:
    """
    A bit set implementation.
    """
    def __init__(self, n=64):
        """
        Initializes a bit set with the given number of bits.
        """
        if n < 1:
            raise ValueError("Invalid BitSet size.")
        self.n = n
        self.bits = [0] * ((n + BitSet.word_size() - 1) // BitSet.word_size())

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        self.set(index, value)
    
    @staticmethod
    def word_size():
        """
        Returns the number of bits in a word.
        """
        return sys.maxsize.bit_length()

    def get(self, bitIndex):
        """
        Returns the value of the bit at the specified index.
        """
        if bitIndex >= self.n:
            raise IndexError("Index out of bounds")
        return (self.bits[bitIndex // BitSet.word_size()] & (1 << (bitIndex % BitSet.word_size()))) != 0

    def set(self, bitIndex, value=True):
        """
        Sets the bit at the specified index to the specified value.
        """
        if bitIndex >= self.n:
            raise IndexError("Index out of bounds")
        if value:
            self.bits[bitIndex // BitSet.word_size()] |= 1 << (bitIndex % BitSet.word_size())
        else:
            self.bits[bitIndex // BitSet.word_size()] &= ~(1 << (bitIndex % BitSet.word_size()))

    def clear(self, bitIndex):
        """
        Sets the bit at the specified index to false.
        """
        self.bits[bitIndex // BitSet.word_size()] &= ~(1 << (bitIndex % BitSet.word_size()))

    def flip(self, bitIndex):
        """
        Toggles the bit at the specified index.
        """
        if bitIndex // BitSet.word_size() < len(self.bits):
            self.bits[bitIndex // BitSet.word_size()] ^= 1 << (bitIndex % BitSet.word_size())

    def next_set_bit(self, fromIndex):
        for i in range(fromIndex, self.n):
            if self[i] == 1:
                return i
        return -1

    def next_clear_bit(self, fromIndex):
        for i in range(fromIndex, self.n):
            if self[i] == 0:
                return i
        return -1

    def previous_set_bit(self, fromIndex):
        for i in range(fromIndex, -1, -1):
            if self[i] == 1:
                return i
        return -1

    def previous_clear_bit(self, fromIndex):
        for i in range(fromIndex, -1, -1):
            if self[i] == 0:
                return i
        return -1
    
    def to_bitstring(self):
        return "".join("1" if self.get(self.n-(i+1)) else "0" for i in range(self.n))
    
    def __str__(self):
        return self.to_bitstring()

    def cardinality(self):
        """
        Returns the number of bits set to true in the bit set.
        """
        return sum(bin(self.bits[i]).count('1') for i in range(len(self.bits)))

    def and_(self, bitSet):
        """
        Performs a logical AND operation on this bit set and the specified bit set.
        """
        self.bits = [self.bits[i] & bitSet.bits[i] for i in range(len(self.bits))]

    def or_(self, bitSet):
        """
        Performs a logical OR operation on this bit set and the specified bit set.
        """
        self.bits = [self.bits[i] | bitSet.bits[i] for i in range(len(self.bits))]

    def xor(self, bitSet):
        """
        Performs a logical XOR operation on this bit set and the specified bit set.
        """
        self.bits = [self.bits[i] ^ bitSet.bits[i] for i in range(len(self.bits))]

    def __eq__(self, obj):
        """
        Returns true if the specified object is equal to this bit set.
        """
        if isinstance(obj, BitSet):
            return self.bits == obj.bits
        return False

    def copy(self):
        """
        Returns a clone of the bit set.
        """
        o = BitSet(self.n)
        o.bits = self.bits.copy()
        return o
    
    def iter_search(self, value):
        for i in range(self.n):
            if self.get(i) == value:
                yield i

    def to_array(self):
        return [i for i in self.iter_search(1)]

    def to_binary_array(self):
        return [1 if self.get(i)==True else 0 for i in range(self.n)]
    
    def rotate(self, t):
        k = t
        while k < 0:
            k += self.n
        while k >= self.n:
            k -= self.n
        x = BitSet(self.n)
        for i in range(self.n):
            x[i] = self[(i - k + self.n) % self.n]
        return x
    
    def union(self, other):
        result = BitSet(self.n)
        for i in range(self.n):
            result.set(i, self.get(i) or other.get(i))
        return result

    def intersection(self, other):
        result = BitSet(self.n)
        for i in range(self.n):
            result.set(i, self.get(i) and other.get(i))
        return result

    def minus(self, other):
        result = BitSet(self.n)
        for i in range(self.n):
            result.set(i, self.get(i) and not other.get(i))
        return result

    @staticmethod
    def from_binary_array(bitarray):
        """
        Initializes the bit set with the specified array of bits.
        """
        bs = BitSet(len(bitarray))
        for i in range(bs.n):
            bs[i] = (bitarray[i] == True)
        return bs
    
    @staticmethod
    def from_bitstring(bitstring):
        o = BitSet(len(bitstring))
        for i in range(o.n):
            o.set(o.n-(i+1), bitstring[i]=="1")
        return o
    
    def intersects(self, bitSet):
        """
        Returns true if the specified bit set has any bits set to true that are also set to true in this bit set.
        """
        for i in range(len(self.bits)):
            if self.bits[i] & bitSet.bits[i]:
                return True
        return False

    def is_empty(self):
        """
        Returns true if the bit set has no bits set to true.
        """
        return all(bit == 0 for bit in self.bits)
    
    def resize(self, newSize):
        """
        Resizes the bit set to the specified number of bits.
        """
        if newSize < 1:
            raise ValueError("Invalid BitSet size")
        
        if newSize > self.n:
            newBits = [0] * ((newSize + BitSet.word_size() - 1) // BitSet.word_size())
            for i,v in enumerate(self.bits):
                newBits[i]=v
            self.n = newSize
            self.bits = newBits
        elif newSize < self.n:
            self.n = newSize
            while len(self.bits) > ((self.n + (BitSet.word_size() - 1)) // BitSet.word_size()):
                self.bits.pop()

    def __lt__(self, other):
        return self.compare(other) == -1
    
    def compare(self, other):
        """
        Compares this bit set to the specified bit set.
        Returns a negative integer if this bit set is less than the specified bit set,
        zero if they are equal, and a positive integer if this bit set is greater than the specified bit set.
        """
        if not isinstance(other, BitSet):
            raise ValueError("Can only compare with another BitSet")
        min_n = min(self.n, other.n)
        for i in range(min_n):
            if(self[i] < other[i]):
                return -1
            if(self[i] > other[i]):
                return 1
        if(self.n == other.n):
            return 0
        if(self.n > other.n):
            return 1
        return -1
