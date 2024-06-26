import unittest
from data_structures.bitset import BitSet

class BitSet_test(unittest.TestCase):
    def test_BitSet_init(self):
        bs = BitSet()
        self.assertEqual(bs.n, 64)

    def test_BitSet_set(self):
        bs = BitSet()
        bs.set(10)
        self.assertTrue(bs.get(10))

    def test_BitSet_clear(self):
        bs = BitSet()
        bs.set(10)
        bs.clear(10)
        self.assertFalse(bs.get(10))

    def test_rotate(self):
        b = BitSet(5)
        b.set(0, True)
        b.set(1, True)
        rotated = b.rotate(-1)
        self.assertEqual(rotated.to_binary_array(), [1, 0, 0, 0, 1])

    def test_intersection(self):
        b1 = BitSet(5)
        b1.set(0, True)
        b1.set(1, True)
        b2 = BitSet(5)
        b2.set(0, True)
        b2.set(2, True)
        self.assertEqual(b1.intersection(b2).to_binary_array(), [1, 0, 0, 0, 0])

    def test_minus(self):
        b1 = BitSet(5)
        b1.set(0, True)
        b1.set(1, True)
        b2 = BitSet(5)
        b2.set(0, True)
        b2.set(2, True)
        self.assertEqual(b1.minus(b2).to_binary_array(), [0, 1, 0, 0, 0])

    def test_union(self):
        b1 = BitSet(5)
        b1.set(0, True)
        b1.set(2, True)

        b2 = BitSet(5)
        b2.set(1, True)
        b2.set(2, True)
        b2.set(3, True)

        b3 = b1.union(b2)

        self.assertTrue(b3.get(0))
        self.assertTrue(b3.get(1))
        self.assertTrue(b3.get(2))
        self.assertTrue(b3.get(3))
        self.assertFalse(b3.get(4))

    def test_BitSet_flip(self):
        bs = BitSet()
        bs.flip(10)
        self.assertTrue(bs.get(10))
        bs.flip(10)
        self.assertFalse(bs.get(10))

    def test_BitSet_next_set_bit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.next_set_bit(5), 10)

    def test_BitSet_next_clear_bit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.next_clear_bit(5), 5)

    def test_BitSet_previous_set_bit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.previous_set_bit(15), 10)

    def test_BitSet_previous_clear_bit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.previous_clear_bit(15), 15)

    def test_BitSet_cardinality(self):
        bs = BitSet()
        bs.set(10)
        bs.set(20)
        self.assertEqual(bs.cardinality(), 2)

    def test_BitSet_and(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = BitSet()
        bs2.set(20)
        bs1.and_(bs2)
        self.assertFalse(bs1.get(10))

    def test_BitSet_or(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = BitSet()
        bs2.set(20)
        bs1.or_(bs2)
        self.assertTrue(bs1.get(10))
        self.assertTrue(bs1.get(20))

    def test_BitSet_xor(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = BitSet()
        bs2.set(20)
        bs1.xor(bs2)
        self.assertTrue(bs1.get(10))
        self.assertTrue(bs1.get(20))

    def test_BitSet_equals(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = BitSet()
        bs2.set(10)
        self.assertTrue(bs1 == bs2)

    def test_BitSet_copy(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = bs1.copy()
        self.assertTrue(bs2.get(10))

    def test_BitSet_intersects(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = BitSet()
        bs2.set(10)
        self.assertTrue(bs1.intersects(bs2))

    def test_BitSet_is_empty(self):
        bs = BitSet()
        self.assertTrue(bs.is_empty())

    def test_BitSet_get_set(self):
        bs = BitSet(128)

        # Test setting and getting individual bits
        for i in range(128):
            bs.set(i)
            self.assertTrue(bs.get(i))
            bs.clear(i)
            self.assertFalse(bs.get(i))

        # Test setting and getting multiple bits at once
        bs.set(0)
        bs.set(5)
        self.assertTrue(bs.get(0))
        self.assertTrue(bs.get(5))

        # Test clearing multiple bits at once
        bs.clear(0)
        bs.clear(64)
        self.assertFalse(bs.get(0))
        self.assertFalse(bs.get(64))

        # Test setting and getting bits out of range
        with self.assertRaises(IndexError):
            bs.set(128)
        with self.assertRaises(IndexError):
            bs.get(128)

        # Test setting and getting bits with invalid indices
        with self.assertRaises(TypeError):
            bs.set('a')
        with self.assertRaises(TypeError):
            bs.get('a')

    def test_to_string(self):
        bitSet = BitSet(8)
        bitSet.set(0)
        bitSet.set(2)
        bitSet.set(4)
        bitSet.set(6)
        self.assertEqual(bitSet.__str__(), "01010101")

    def test_from_bitstring(self):
        bs = BitSet.from_bitstring("01010101")
        self.assertTrue(bs[0])
        self.assertFalse(bs[1])
        self.assertTrue(bs[2])
        self.assertFalse(bs[3])
        self.assertTrue(bs[4])
        self.assertFalse(bs[5])
        self.assertTrue(bs[6])
        self.assertFalse(bs[7])
        self.assertEqual(bs.n,8)

    def test_from_array(self):
        bs = BitSet.from_binary_array([0,1,0,1,1]);
        self.assertEqual(bs.__str__(),"11010")

    def test_lt(self):
        bs1 = BitSet(5)
        bs1.set(0, True)
        bs1.set(2, True)

        bs2 = BitSet(5)
        bs2.set(0, True)
        bs2.set(1, True)
        bs2.set(2, True)

        self.assertTrue(bs1 < bs2)

        bs3 = BitSet(5)
        bs3.set(0, True)
        bs3.set(2, True)

        self.assertFalse(bs1 < bs3)

    def test_to_array(self):
        c = BitSet(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(c.to_array(), [0, 1])

    def test_from_binary_array(self):
        b = BitSet.from_binary_array([1, 1, 0, 0, 0])
        self.assertEqual(b.to_binary_array(), [1, 1, 0, 0, 0])

    def test_from_bitstring(self):
        b = BitSet.from_bitstring("00011")
        self.assertEqual(b.to_binary_array(), [1, 1, 0, 0, 0])

    def test_to_binary_array(self):
        c = BitSet(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(c.to_binary_array(), [1, 1, 0, 0, 0])

    def test_resize_larger(self):
        bs = BitSet(100)
        # Fill the bitset with some values
        for i in range(bs.n): 
            if i % 2 == 0:
                bs.set(i, True)

        # Resize to a larger size
        bs.resize(200)
        self.assertEqual(len(bs.bits), ((200 + BitSet.word_size() - 1) // BitSet.word_size()))
 

    def test_resize_smaller(self): 
        bs = BitSet(100)
         # Fill the bitset with some values
        for i in range(bs.n):
            if i % 2 == 0:
                bs.set(i, True)

         # Resize to a smaller size
        bs.resize(50)
        self.assertEqual(len(bs.bits), ((50 + BitSet.word_size() - 1) // BitSet.word_size()))

    def test_resize_same(self): 
        bs = BitSet(100)
         # Fill the bitset with some values
        for i in range(bs.n):
            if i % 2 == 0:
                bs.set(i, True)

         # Resize to the same size
        bs.resize(100)
        self.assertEqual(len(bs.bits), ((100 + BitSet.word_size() - 1) // BitSet.word_size()))

    def test_resize_invalid(self):
        bs = BitSet(100)
        with self.assertRaises(ValueError): 
            bs.resize(-10)
