from max_binary_heap import *
import unittest

class TestMasBinaryHeap(unittest.TestCase):

    def test_insert(self):
        nodes = [90,100,80,95,88,75,60]
        max_binary_heap = MaxBinaryHeap(nodes)
        self.assertEqual(max_binary_heap.heap, [100,95,80,90,88,75,60])
        max_binary_heap.insert(93)
        max_binary_heap.insert(85)
        self.assertEqual(max_binary_heap.heap, [100,95,80,93,88,75,60,90,85])

    def test_get_max(self):
        nodes = [90,100,80,95,88,75,60]
        max_binary_heap = MaxBinaryHeap(nodes)
        self.assertEqual(max_binary_heap.get_max(),100)
        max_binary_heap.insert(200)
        self.assertEqual(max_binary_heap.get_max(),200)
        max_binary_heap.insert(1300)
        self.assertEqual(max_binary_heap.get_max(),1300)

    def test_delete_min(self):
        nodes = [90,100,80,95,88,75,60]
        max_binary_heap = MaxBinaryHeap(nodes)
        max_binary_heap.delete_max()
        self.assertEqual(max_binary_heap.heap, [95,90,80,60,88,75])
        max_binary_heap.delete_max()
        self.assertEqual(max_binary_heap.heap,[90,88,80,60,75])

if __name__ == '__main__':
    unittest.main()
