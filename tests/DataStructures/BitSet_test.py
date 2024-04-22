import unittest
from DataStructures.BitSet import BitSet

class BitSet_test(unittest.TestCase):
    def test_BitSet_init(self):
        bs = BitSet()
        self.assertEqual(bs.size, 64)

    def test_BitSet_set(self):
        bs = BitSet()
        bs.set(10)
        self.assertTrue(bs.get(10))

    def test_BitSet_clear(self):
        bs = BitSet()
        bs.set(10)
        bs.clear(10)
        self.assertFalse(bs.get(10))

    def test_BitSet_flip(self):
        bs = BitSet()
        bs.flip(10)
        self.assertTrue(bs.get(10))
        bs.flip(10)
        self.assertFalse(bs.get(10))

    def test_BitSet_nextSetBit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.nextSetBit(5), 10)

    def test_BitSet_nextClearBit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.nextClearBit(5), 5)

    def test_BitSet_previousSetBit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.previousSetBit(15), 10)

    def test_BitSet_previousClearBit(self):
        bs = BitSet()
        bs.set(10)
        self.assertEqual(bs.previousClearBit(15), 14)

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
        self.assertTrue(bs1.equals(bs2))

    def test_BitSet_clone(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = bs1.clone()
        self.assertTrue(bs2.get(10))

    def test_BitSet_intersects(self):
        bs1 = BitSet()
        bs1.set(10)
        bs2 = BitSet()
        bs2.set(10)
        self.assertTrue(bs1.intersects(bs2))

    def test_BitSet_isEmpty(self):
        bs = BitSet()
        self.assertTrue(bs.isEmpty())

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
        bs.set(64)
        self.assertTrue(bs.get(0))
        self.assertTrue(bs.get(64))

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
    def test_toString(self):
        bitSet = BitSet(8)
        bitSet.set(0)
        bitSet.set(2)
        bitSet.set(4)
        bitSet.set(6)
        self.assertEqual(bitSet.toString(), "10101010")
        
if __name__ == '__main__':
    unittest.main()