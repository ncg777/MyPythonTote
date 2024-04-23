import unittest
import data_structures
import data_structures.bitset
from data_structures.combination import Combination

class TestCombination(unittest.TestCase):

    def test_init(self):
        c = Combination(5)
        self.assertEqual(c.n, 5)

    def test_symmetric_difference(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(2, True)
        self.assertEqual(c1.symmetric_difference(c2).to_binary_array(), [0, 1, 1, 0, 0])

    def test_eq(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        print(c1.to_binary_array)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(1, True)
        self.assertEqual(c1, c2)

    def test_hash(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(1, True)
        self.assertEqual(hash(c1), hash(c2))

    def test_to_bitstring(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(c.to_bitstring(), '00011')

    def test_str(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(str(c), '{0, 1}')

    def test_from_binary_array(self):
        b = Combination.from_binary_array([1, 1, 0, 0, 0])
        self.assertEqual(b.to_binary_array(), [1, 1, 0, 0, 0])

    def test_from_bitstring(self):
        c = Combination.from_bitstring("00011")
        self.assertEqual(c.to_binary_array(), [1, 1, 0, 0, 0])

    def test_from_bitset(self):
        bs = data_structures.bitset.BitSet.from_bitstring("00011")
        c = Combination.from_bitset(bs)
        self.assertEqual(c.to_binary_array(), [1, 1, 0, 0, 0])

    def test_rotate(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        rotated = c.rotate(-1)
        self.assertEqual(rotated.to_binary_array(), [1, 0, 0, 0, 1])

    def test_intersection(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(2, True)
        self.assertEqual(c1.intersection(c2).to_binary_array(), [1, 0, 0, 0, 0])

    def test_minus(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(2, True)
        self.assertEqual(c1.minus(c2).to_binary_array(), [0, 1, 0, 0, 0])

    def test_union(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(2, True)

        c2 = Combination(5)
        c2.set(1, True)
        c2.set(2, True)
        c2.set(3, True)

        c3 = c1.union(c2)

        self.assertTrue(c3.get(0))
        self.assertTrue(c3.get(1))
        self.assertTrue(c3.get(2))
        self.assertTrue(c3.get(3))
        self.assertFalse(c3.get(4))

if __name__ == '__main__':
    unittest.main()