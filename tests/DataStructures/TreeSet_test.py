import unittest
from DataStructures.TreeSet import TreeSet

class TreeSet_test(unittest.TestCase):

    def test_init(self):
        # Test empty TreeSet
        ts = TreeSet()
        self.assertEqual(len(ts), 0)

        # Test TreeSet with elements
        ts = TreeSet([3, 1, 2, 4, 5])
        self.assertEqual(len(ts), 5)
        self.assertEqual(list(ts), [1, 2, 3, 4, 5])

    def test_add(self):
        ts = TreeSet()
        ts.add(1)
        self.assertEqual(len(ts), 1)
        self.assertEqual(list(ts), [1])

        ts.add(2)
        self.assertEqual(len(ts), 2)
        self.assertEqual(list(ts), [1, 2])

        ts.add(1)
        self.assertEqual(len(ts), 2)
        self.assertEqual(list(ts), [1, 2])

    def test_remove(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        ts.remove(3)
        self.assertEqual(len(ts), 4)
        self.assertEqual(list(ts), [1, 2, 4, 5])

        ts.remove(6)
        self.assertEqual(len(ts), 4)
        self.assertEqual(list(ts), [1, 2, 4, 5])

    def test_contains(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertTrue(ts.contains(1))
        self.assertFalse(ts.contains(6))

    def test_size(self):
        ts = TreeSet()
        self.assertEqual(ts.size(), 0)

        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.size(), 5)

    def test_isEmpty(self):
        ts = TreeSet()
        self.assertTrue(ts.isEmpty())

        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertFalse(ts.isEmpty())

    def test_iterator(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(list(iter(ts)), [1, 2, 3, 4, 5])

    def test_descendingIterator(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(list(ts.descendingIterator()), [5, 4, 3, 2, 1])
        
    def test_subSet(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(list(ts.subSet(2, True, 4, True)), [2, 3, 4])

    def test_headSet(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(list(ts.headSet(3, True)), [1, 2, 3])

    def test_tailSet(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(list(ts.tailSet(3, True)), [3, 4, 5])

    def test_first(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.first(), 1)

    def test_last(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.last(), 5)

    def test_lower(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.lower(3), 2)

    def test_floor(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.floor(3), 3)

    def test_ceiling(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.ceiling(3), 3)

    def test_higher(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.higher(3), 4)

    def test_pollFirst(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.pollFirst(), 1)
        self.assertEqual(len(ts), 4)
        self.assertEqual(list(ts), [2, 3, 4, 5])

    def test_pollLast(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        self.assertEqual(ts.pollLast(), 5)
        self.assertEqual(len(ts), 4)
        self.assertEqual(list(ts), [1, 2, 3, 4])

    def test_copyOf(self):
        ts = TreeSet([1, 2, 3, 4, 5])
        ts_copy = ts.copyOf()
        self.assertEqual(len(ts_copy), 5)
        self.assertEqual(list(ts_copy), [1, 2, 3, 4, 5])

        ts.add(6)
        self.assertEqual(len(ts_copy), 5)
        self.assertEqual(list(ts_copy), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()