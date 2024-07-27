from math import log2, floor

class MaxBinaryHeap:
    def __init__(self, values: list) -> None:
        self.heap = values
        self.heap_size = len(self.heap)
        self.build_heap()

    def build_heap(self):
        start_index = self.heap_size // 2 - 1
        for i in range(start_index, -1, -1):
            self.__heapify(i)

    def __heapify(self, index = 0):
        largest = index
        left_child = self.left_child_index(index)
        right_child = self.right_child_index(index)

        if(left_child < self.heap_size and self.heap[left_child] > self.heap[largest]):
            largest = left_child
        
        if(right_child < self.heap_size and self.heap[right_child] > self.heap[largest]):
            largest = right_child

        if(largest != index):
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.__heapify(largest)

    def left_child_index(self, index: int):
        return (2*index + 1)

    def right_child_index(self, index: int):
        return (2*index + 2)
    
    def parent_index(self, index: int):
        return (index-1)//2
    
    def insert(self, value):
        if value not in self.heap:
            self.heap.append(value)
            self.heap_size += 1
            self.build_heap()
        else:
            pass

    def get_max(self):
        return self.heap[0]
    
    def delete_max(self):
        self.heap[0] = self.heap[self.heap_size-1]
        del(self.heap[self.heap_size-1])
        self.heap_size -= 1
        self.__heapify()

    def print_heap(self):
        print(self.heap_size)
        for node in self.heap:
            parent_index = self.heap.index(node)
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            print(f"Rodzic : {node}")
            if left_child_index < self.heap_size:
                print(f"\tLewe dziecko: {self.heap[left_child_index]}")
            if right_child_index < self.heap_size:
                print(f"\tPrawe dziecko: {self.heap[right_child_index]}")

nodes = [50,100,70,60,55,75,85]

max_heap = MaxBinaryHeap(nodes)

print(max_heap.heap)

print(f'\n\nTest usuwania')
max_heap.delete_max()
print(f'Kopiec po usunięciu maxa : {max_heap.heap}')

print(f'Test funkcji print_heap')

max_heap.print_heap()

max_heap.insert(20)

max_heap.print_heap()

max_heap.insert(65)

max_heap.print_heap()