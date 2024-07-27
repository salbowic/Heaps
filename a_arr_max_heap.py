class AaryHeap:
    def __init__(self, values = None, A = 2):
        self.heap = values
        self.heap_size = len(values)
        self.A = A
        self.build_heap()

    def build_heap(self):
        start_index = self.heap_size // self.A - 1
        for i in range(start_index, -1, -1):
            self.__heapify_down(i)

    def __heapify_down(self, index: int):
        while True:
            children = self.get_children_indexes(index)
            max_child = -1
            max_child_index = 0
            for i in range(0, self.A):
                if children[i] != -1 and self.heap[children[i]] > max_child:
                    max_child_index = children[i]
                    max_child = self.heap[children[i]]
 
            if max_child == -1:
                break
    
            if self.heap[index] < self.heap[max_child_index]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
    
            index = max_child_index


    def parent_index(self, index: int):
        return (index-1) // self.A
    
    def get_children_indexes(self, parent_index):
        return [self.A * parent_index + i if self.A * parent_index + i < self.heap_size else -1 for i in range(1, self.A + 1)]


    def __heapify_up(self, index: int):
        parent_index = self.parent_index(index)
        while parent_index >= 0:
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
                parent_index = self.parent_index(index)
            else:
                break
    
    def insert(self, value):
        if value not in self.heap:
            self.heap.append(value)
            self.heap_size += 1
            self.__heapify_up(self.heap_size - 1)
        else:
            pass
    
    
    def delete_root(self):
        self.heap[0] = self.heap[self.heap_size-1]
        del(self.heap[self.heap_size-1])
        self.heap_size -= 1
        self.__heapify_down(0)

    def get_root(self):
        return self.heap[0]
    
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

  


three_heap = AaryHeap([50,100,70,60,55,75,85],3)

 
print("Built Heap:")
print(three_heap.heap)
print(three_heap.print_heap())
three_heap.delete_root()
print(three_heap.heap)

three_heap.insert(130)
three_heap.print_heap()