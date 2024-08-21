import unittest
from generators.combination_generator import CombinationGenerator

class TestCombinationGenerator(unittest.TestCase):

    def test_init(self):
        gen = CombinationGenerator(5, 3)
        self.assertIsNotNone(gen)

    def test_next(self):
        gen = CombinationGenerator(5, 3)
        self.assertEqual(next(gen).to_binary_array(), [True, True, True, False, False])

    def test_has_next(self):
        gen = CombinationGenerator(5, 3)
        self.assertTrue(hasattr(gen, '__next__'))

    def test_all_elements(self):
        gen = CombinationGenerator(3, 2)
        self.assertEqual(next(gen).to_binary_array(), [True, True, False])
        self.assertEqual(next(gen).to_binary_array(), [True, False, True])
        self.assertEqual(next(gen).to_binary_array(), [False, True, True])

    def test_combinations_count(self):
        gen = CombinationGenerator(5, 3)
        count = 0
        for _ in gen:
            count += 1
        self.assertEqual(count, 10)

if __name__ == '__main__':
    unittest.main()