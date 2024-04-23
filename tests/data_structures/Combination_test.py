import unittest
from data_structures.combination import Combination

class TestCombination(unittest.TestCase):

    def test_init(self):
        c = Combination(5)
        self.assertEqual(c.n, 5)

    def test_symmetricDifference(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(2, True)
        self.assertEqual(c1.symmetric_difference(c2).asBinarySequence(), [0, 1, 1, 0, 0])

    def test_eq(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        print(c1.asBinarySequence)
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

    def test_toBinaryString(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(c.to_bitstring(), '11000')

    def test_str(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(str(c), '{0, 1}')

    def test_asSequence(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(c.asSequence(), [0, 1])

    def test_asBinarySequence(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        self.assertEqual(c.asBinarySequence(), [1, 1, 0, 0, 0])

    def test_fromBinarySequence(self):
        c = Combination.fromBinarySequence([1, 1, 0, 0, 0])
        self.assertEqual(c.asBinarySequence(), [1, 1, 0, 0, 0])

    def test_rotate(self):
        c = Combination(5)
        c.set(0, True)
        c.set(1, True)
        rotated = c.rotate(1)
        self.assertEqual(rotated.asBinarySequence(), [0, 1, 1, 0, 0])

    def test_intersection(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(2, True)
        self.assertEqual(c1.intersection(c2).asBinarySequence(), [1, 0, 0, 0, 0])

    def test_minus(self):
        c1 = Combination(5)
        c1.set(0, True)
        c1.set(1, True)
        c2 = Combination(5)
        c2.set(0, True)
        c2.set(2, True)
        self.assertEqual(c1.minus(c2).asBinarySequence(), [0, 1, 0, 0, 0])

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