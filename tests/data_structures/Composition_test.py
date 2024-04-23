import unittest
import data_structures.composition

class TestComposition(unittest.TestCase):

    def test_from_combination(self):
        c = data_structures.combination.Combination(5)
        c.set(0)
        c.set(2)
        c.set(4)
        comp = data_structures.composition.Composition.from_combination(c)
        self.assertEqual(comp.to_array(), [2, 2, 1])

    def test_from_array(self):
        comp = data_structures.composition.Composition.from_array([1, 2, 1])
        self.assertEqual(comp.to_array(), [1, 2, 1])

    def test_get_total(self):
        comp = data_structures.composition.Composition(5)
        self.assertEqual(comp.get_total(), 5)

    def test_to_array(self):
        comp = data_structures.composition.Composition(5)
        comp.set(0)
        comp.set(2)
        self.assertEqual(comp.to_array(), [1,2,2])

    def test_to_combination(self):
        comp = data_structures.composition.Composition(5)
        comp.set(0)
        comp.set(2)
        c = comp.to_combination()
        self.assertEqual(c.to_binary_array(), [1, 1, 0, 1, 0])

if __name__ == '__main__':
    unittest.main()