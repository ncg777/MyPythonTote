class BitSet:
    """
    A bit set implementation.
    """
    def __init__(self, n=64):
        """
        Initializes a bit set with the given number of bits.
        """
        self.bits = [0] * ((n + 63) // 64)

    def size(self):
        """
        Returns the number of bits in the bit set.
        """
        return len(self.bits) * 64

    def length(self):
        """
        Returns the number of bits in the bit set.
        """
        return self.size()

    def get(self, bitIndex):
        """
        Returns the value of the bit at the specified index.
        """
        return (self.bits[bitIndex // 64] & (1 << (bitIndex % 64))) != 0

    def set(self, bitIndex, value=1):
        """
        Sets the bit at the specified index to the specified value.
        """
        self.bits[bitIndex // 64] |= 1 << (bitIndex % 64)

    def clear(self, bitIndex):
        """
        Sets the bit at the specified index to false.
        """
        self.bits[bitIndex // 64] &= ~(1 << (bitIndex % 64))

    def flip(self, bitIndex):
        """
        Toggles the bit at the specified index.
        """
        if bitIndex // 64 < len(self.bits):
            self.bits[bitIndex // 64] ^= 1 << (bitIndex % 64)

    def nextSetBit(self, fromIndex):
        """
        Returns the index of the first bit that is set to true that occurs on or after the specified starting index.
        """
        for i in range(fromIndex // 64, len(self.bits)):
            if self.bits[i] != 0:
                return i * 64 + self.bits[i].bit_length() - 1
        return -1

    def nextClearBit(self, bitIndex):
        while bitIndex < self.size():
            if not self.get(bitIndex):
                return bitIndex
            bitIndex += 1
        return self.size()

    def previousSetBit(self, bitIndex):
        while bitIndex >= 0:
            if self.get(bitIndex):
                return bitIndex
            bitIndex -= 1
        return -1

    def previousClearBit(self, bitIndex):
        bitIndex -= 1
        while bitIndex >= 0:
            if not self.get(bitIndex):
                return bitIndex
            bitIndex -= 1
        return -1

    def toString(self):
        """
        Returns a string representation of the bit set.
        """
        return "{" + ", ".join(str(i) for i in range(self.size()) if self.get(i)) + "}"
    

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

    def equals(self, obj):
        """
        Returns true if the specified object is equal to this bit set.
        """
        if isinstance(obj, BitSet):
            return self.bits == obj.bits
        return False

    def clone(self):
        """
        Returns a clone of the bit set.
        """
        return BitSet(len(self.bits) * 64).fromArray(self.bits)

    def fromArray(self, bits):
        """
        Initializes the bit set with the specified array of bits.
        """
        self.bits = bits
        return self
    
    def intersects(self, bitSet):
        """
        Returns true if the specified bit set has any bits set to true that are also set to true in this bit set.
        """
        for i in range(len(self.bits)):
            if self.bits[i] & bitSet.bits[i]:
                return True
        return False

    def isEmpty(self):
        """
        Returns true if the bit set has no bits set to true.
        """
        return all(bit == 0 for bit in self.bits)
