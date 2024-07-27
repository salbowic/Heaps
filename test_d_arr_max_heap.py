from a_arr_max_heap import *
import unittest

class TestAaryHeap(unittest.TestCase):

    def test_2_insert_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 2)
        self.assertEqual(dary_heap.heap, [100, 95, 80, 90, 88, 75, 60])
        dary_heap.insert(93)
        dary_heap.insert(85)
        self.assertEqual(dary_heap.heap, [100, 95, 80, 93, 88, 75, 60, 90, 85])

    def test_2_get_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 2)
        self.assertEqual(dary_heap.get_root(), 100)
        dary_heap.insert(200)
        self.assertEqual(dary_heap.get_root(), 200)
        dary_heap.insert(1300)
        self.assertEqual(dary_heap.get_root(), 1300)

    def test_2_delete_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 2)
        dary_heap.delete_root()
        self.assertEqual(dary_heap.heap, [95, 90, 80, 60, 88, 75])
        dary_heap.delete_root()
        self.assertEqual(dary_heap.heap, [90, 88, 80, 60, 75])

# d = 3

    def test_3_insert_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 3)
        self.assertEqual(dary_heap.heap, [100, 90, 80, 95, 88, 75 ,60])
        dary_heap.insert(93)
        dary_heap.insert(86)
        dary_heap.insert(85)
        self.assertEqual(dary_heap.heap, [100, 90, 93, 95, 88, 75 ,60, 80, 86, 85])

    def test_3_get_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 3)
        self.assertEqual(dary_heap.get_root(), 100)
        dary_heap.insert(200)
        self.assertEqual(dary_heap.get_root(), 200)
        dary_heap.insert(1300)
        self.assertEqual(dary_heap.get_root(), 1300)

    def test_3_delete_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 3)
        dary_heap.delete_root()
        self.assertEqual(dary_heap.heap, [95, 90, 80, 60, 88, 75])
        dary_heap.delete_root()
        self.assertEqual(dary_heap.heap, [90, 88, 80, 60, 75])

# d = 4

    def test_4_insert_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60, 120, 25, 30]
        dary_heap = AaryHeap(nodes, 4)
        self.assertEqual(dary_heap.heap, [120, 100, 80, 95, 88, 75, 60, 90, 25, 30])
        dary_heap.insert(93)
        dary_heap.insert(86)
        dary_heap.insert(85)
        dary_heap.insert(98)
        dary_heap.insert(21)
        dary_heap.insert(10)
        self.assertEqual(dary_heap.heap, [120, 100, 93, 98, 88, 75, 60, 90, 25, 30, 80, 86, 85, 95, 21, 10])

    def test_4_get_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60]
        dary_heap = AaryHeap(nodes, 4)
        self.assertEqual(dary_heap.get_root(), 100)
        dary_heap.insert(200)
        self.assertEqual(dary_heap.get_root(), 200)
        dary_heap.insert(1300)
        self.assertEqual(dary_heap.get_root(), 1300)

    def test_4_delete_max(self):
        nodes = [90, 100, 80, 95, 88, 75, 60, 120, 25, 30]
        dary_heap = AaryHeap(nodes, 4)
        dary_heap.delete_root()
        self.assertEqual(dary_heap.heap, [100, 90, 80, 95, 88, 75, 60, 30, 25])
        dary_heap.delete_root()
        self.assertEqual(dary_heap.heap, [95, 90, 80, 25, 88, 75, 60, 30] )


if __name__ == '__main__':
    unittest.main()
