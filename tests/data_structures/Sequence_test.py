import unittest
from data_structures.sequence import Sequence

class TestSequence(unittest.TestCase):

    def test_to_array(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.to_array(), [1, 2, 3, 4, 5])

    def test_calc_interval_vector(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.calc_interval_vector(), {1: [0, 0], 2: [0, 0], 3: [0, 0], 4: [0, 0], 5: [0, 0]})

    def test_contains(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertTrue(seq.contains(3))
        self.assertFalse(seq.contains(6))

    def test_antidifference(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.antidifference(2).to_array(), [2, 3, 5, 8, 12, 17])

    def test_difference(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.difference().to_array(), [1, 1, 1, 1])

    def test_cyclical_difference(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.cyclical_difference().to_array(), [-4, 1, 1, 1, 1])

    def test_cyclical_antidifference(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.cyclical_antidifference(2).to_array(), [7, 8, 10, 13, 17])

    def test_reversed(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.reversed().to_array(), [5, 4, 3, 2, 1])

    def test_get(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.get(2), 3)

    def test_size(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.size(), 5)

    def test_add(self):
        seq = Sequence([1, 2, 3, 4, 5])
        seq.add(6)
        self.assertEqual(seq.to_array(), [1, 2, 3, 4, 5, 6])

    def test_set(self):
        seq = Sequence([1, 2, 3, 4, 5])
        seq.set(2, 6)
        self.assertEqual(seq.to_array(), [1, 2, 6, 4, 5])

    def test_distinct(self):
        seq = Sequence([1, 2, 2, 3, 3, 3, 4, 5])
        self.assertEqual(seq.distinct(), {1, 2, 3, 4, 5})

    def test_count(self):
        seq = Sequence([1, 2, 2, 3, 3, 3, 4, 5])
        self.assertEqual(seq.count(3), 3)

    def test_get_mean(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.get_mean(), 3.0)

    def test_get_std_dev(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertAlmostEqual(seq.get_std_dev(), 1.4142135623730951)

    def test_rotate(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.rotate(-2).to_array(), [3, 4, 5, 1, 2])

    def test_map_ordinals_unipolar(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.map_ordinals_unipolar(), {1: 0, 2: 1, 3: 2, 4: 3, 5: 4})

    def test_to_ordinals_unipolar(self):
        seq = Sequence([1, 2, 3, 4, 5])
        self.assertEqual(seq.to_ordinals_unipolar().to_array(), [0, 1, 2, 3, 4])

    def test_map_ordinals_bipolar(self):
        seq = Sequence([-2, -1, 0, 1, 2])
        self.assertEqual(seq.map_ordinals_bipolar(), {0: 0, 1: 1, 2: 2, -1: -1, -2: -2})

    def test_to_ordinals_bipolar(self):
        seq = Sequence([-2, -1, 0, 1, 2])
        self.assertEqual(seq.to_ordinals_bipolar().to_array(), [-2, -1, 0, 1, 2])

    def test_map_with_dict(self):
        seq = Sequence([1, 2, 3, 4, 5])
        mapping = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
        self.assertEqual(seq.map_with_dict(mapping).to_array(), [10, 20, 30, 40, 50])

    def test_permutate(self):
        seq = Sequence([1, 2, 3, 4, 5])
        s = Sequence([4, 3, 2, 1, 0])
        self.assertEqual(seq.permutate(s).to_array(), [5, 4, 3, 2, 1])

    def test_juxtapose(self):
        seq = Sequence([1, 2, 3, 4, 5])
        s = Sequence([6, 7, 8, 9, 10])
        self.assertEqual(seq.juxtapose(s).to_array(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_get_period(self):
        seq = Sequence([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])
        self.assertEqual(seq.get_period(), 5)

    def test_circular_hold_non_zero(self):
        seq = Sequence([1, 2, 0, 4, 5, 0, 0, 8, 9, 0])
        self.assertEqual(seq.circular_hold_non_zero().to_array(), [1, 2, 2, 4, 5, 5, 5, 8, 9, 9])

if __name__ == 'main':
    unittest.main()