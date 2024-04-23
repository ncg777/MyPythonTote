import unittest
from data_structures.treemap import TreeMap

class TestTreeMap(unittest.TestCase):

    def test_putAndGet(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        self.assertEqual(treeMap.get("key1"), "value1")

    def test_putAll(self):
        treeMap = TreeMap()
        map = {"key1": "value1", "key2": "value2"}
        treeMap.putAll(map)
        self.assertEqual(treeMap.get("key1"), "value1")
        self.assertEqual(treeMap.get("key2"), "value2")

    def test_containsKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        self.assertTrue(treeMap.containsKey("key1"))
        self.assertFalse(treeMap.containsKey("key2"))

    def test_containsValue(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        self.assertTrue(treeMap.containsValue("value1"))
        self.assertFalse(treeMap.containsValue("value2"))

    def test_size(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.size(), 2)

    def test_isEmpty(self):
        treeMap = TreeMap()
        self.assertTrue(treeMap.isEmpty())
        treeMap.put("key1", "value1")
        self.assertFalse(treeMap.isEmpty())

    def test_remove(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.remove("key1")
        self.assertFalse(treeMap.containsKey("key1"))

    def test_keySet(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.keySet(), {"key1", "key2"})

    def test_values(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.values(), ["value1", "value2"])

    def test_entrySet(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.entrySet(), [("key1", "value1"), ("key2", "value2")])

    def test_firstKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.firstKey(), "key1")

    def test_lastKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.lastKey(), "key2")

    def test_floorKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.floorKey("key1"), "key1")
        self.assertEqual(treeMap.floorKey("key2"), "key2")
        self.assertEqual(treeMap.floorKey("key3"), "key2")

    def test_ceilingKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.ceilingKey("key1"), "key1")
        self.assertEqual(treeMap.ceilingKey("key2"), "key2")
        self.assertEqual(treeMap.ceilingKey("key3"), None)

    def test_lowerKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.lowerKey("key1"), None)
        self.assertEqual(treeMap.lowerKey("key2"), "key1")
        self.assertEqual(treeMap.lowerKey("key3"), "key2")

    def test_higherKey(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.higherKey("key1"), "key2")
        self.assertEqual(treeMap.higherKey("key2"), None)
        self.assertEqual(treeMap.higherKey("key3"), None)

    def test_pollFirstEntry(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.pollFirstEntry(), ("key1", "value1"))
        self.assertFalse(treeMap.containsKey("key1"))

    def test_pollLastEntry(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.pollLastEntry(), ("key2", "value2"))
        self.assertFalse(treeMap.containsKey("key2"))

    def test_descendingKeySet(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.descendingKeySet(), ["key2", "key1"])

    def test_descendingMap(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.descendingMap(), {"key2": "value2", "key1": "value1"})

    def test_navigateableKeySet(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.navigateableKeySet(), ["key1", "key2"])

    def test_navigateableEntrySet(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.put("key2", "value2")
        self.assertEqual(treeMap.navigateableEntrySet(), [("key1", "value1"), ("key2", "value2")])

    def test_replace(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.replace("key1", "value1", "newValue")
        self.assertEqual(treeMap.get("key1"), "newValue")

    def test_replace_with_old_value(self):
        treeMap = TreeMap()
        treeMap.put("key1", "value1")
        treeMap.replace("key1", "value1", "newValue")
        self.assertEqual(treeMap.get("key1"), "newValue")

if __name__ == '__main__':
    unittest.main()