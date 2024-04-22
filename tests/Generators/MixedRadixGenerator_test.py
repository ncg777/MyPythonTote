import unittest
from Generators.MixedRadixGenerator import MixedRadixGenerator

class TestMixedRadixGenerator(unittest.TestCase):

    def test_simple_case(self):
        gen = MixedRadixGenerator([2, 2])
        self.assertEqual(next(gen), [0, 0])
        self.assertEqual(next(gen), [0, 1])
        self.assertEqual(next(gen), [1, 0])
        self.assertEqual(next(gen), [1, 1])
        with self.assertRaises(StopIteration):
            next(gen)

    def test_larger_case(self):
        gen = MixedRadixGenerator([3, 4, 2])
        results = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 2, 0], [0, 2, 1], [0, 3, 0], [0, 3, 1],
                   [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [1, 2, 0], [1, 2, 1], [1, 3, 0], [1, 3, 1],
                   [2, 0, 0], [2, 0, 1], [2, 1, 0], [2, 1, 1], [2, 2, 0], [2, 2, 1], [2, 3, 0], [2, 3, 1]]
        for expected in results:
            self.assertEqual(next(gen), expected)
        with self.assertRaises(StopIteration):
            next(gen)

if __name__ == '__main__':
    unittest.main()