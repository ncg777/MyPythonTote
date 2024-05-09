import unittest
from generators.word_permutation_generator import WordPermutationGenerator

class TestWordPermutationGenerator(unittest.TestCase):

    def test_init(self):
        rk = [1, 4, 4, 2]
        gen = WordPermutationGenerator(rk)
        self.assertIsNotNone(gen)

    def test_next(self):
        rk = [1, 4, 4, 2]
        gen = WordPermutationGenerator(rk)
        self.assertEqual(next(gen), [3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0])

    def test_has_next(self):
        rk = [1, 4, 4, 2]
        gen = WordPermutationGenerator(rk)
        self.assertTrue(hasattr(gen, '__next__'))

    def test_next_element(self):
        rk = [1, 4, 4, 2]
        gen = WordPermutationGenerator(rk)
        self.assertEqual(next(gen), [3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 0])
        self.assertEqual(next(gen), [3, 2, 3, 2, 2, 2, 1, 1, 1, 1, 0])

    def test_all_elements(self):
        rk = [2, 3, 2]
        a = list(WordPermutationGenerator(rk))
        self.assertEqual(len(a), 210)

if __name__ == '__main__':
    unittest.main()