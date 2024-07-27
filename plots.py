from a_arr_max_heap import AaryHeap
import time
import matplotlib.pyplot as plt
import random
import gc

def measure_insertion_time_with_gc(heap, values):
    gc_old = gc.isenabled()
    gc.disable()
    start_time = time.perf_counter()
    for value in values:
        heap.insert(value)
    end_time = time.perf_counter()
    if gc_old:
        gc.enable()
    return (end_time - start_time) * 1000

def measure_insertion():
    # Initialize variables for plotting
    heap_sizes = []
    insertion_times = []

    # Pre-initialize the heap with a 10 values
    heap = AaryHeap(values=[random.randint(1, 10_000_000) for _ in range(10)], A=2)

    for step in range(1, 101):  # Loop to increase heap size from 1000 to 100,000 in increments of 1000
        # Generate 1000 random values from 1 to 10,000,000
        random_values = [random.randint(1, 10_000_000) for _ in range(1001)]
        
        # Add 90 of these values to the heap to increase its size by 1000
        for value in random_values[:-10]:
            heap.insert(value)
        
        heap_sizes.append(heap.heap_size)
        # Measure insertion time for the 100th value
        insertion_time = measure_insertion_time_with_gc(heap, random_values[-10:])
        
        # Update the plotting variables
        insertion_times.append(insertion_time)

    # Plot Insertion Time vs. Heap Size (with heap size increasing by 100 each step)
    plt.figure(figsize=(10, 6))
    plt.plot(heap_sizes, insertion_times, linestyle='-', color='b')
    plt.title("Insertion Time vs. Heap Size (Incremental with Random Values)")
    plt.xlabel("Heap Size")
    plt.ylabel("Time to Insert 10 values [ms]")
    plt.grid(True)
    plt.show()

def measure_deletion_time(heap):
    gc_old = gc.isenabled()
    gc.disable()
    start_time = time.perf_counter()
    heap.delete_root()
    end_time = time.perf_counter()
    if gc_old:
        gc.enable()
    return (end_time - start_time) * 1000


def measure_deletion():
    # Initialize variables for plotting
    heap_sizes = []
    deletion_times = []

    heap = AaryHeap(values=[], A=2)

    for step in range(1, 101):  # Loop to increase heap size from 100 to 10,000 in increments of 100
        random_values = [random.randint(1, 1_000_000) for _ in range(101)]
        
        for value in random_values[:-1]:
            heap.insert(value)

        heap_sizes.append(heap.heap_size)

        deletion_time = measure_deletion_time(heap)
        
        # Re-insert a value to keep the heap size balanced
        heap.insert(random_values[100])

        deletion_times.append(deletion_time)

    plt.figure(figsize=(10, 6))
    plt.plot(heap_sizes, deletion_times, marker='o', linestyle='-', color='r')
    plt.title("Deletion Time vs. Heap Size (Incremental with Random Values)")
    plt.xlabel("Heap Size")
    plt.ylabel("Time to Delete One Node [ms]")
    plt.grid(True)
    plt.show()

# Execute the updated measurement function for deletion
def measure_deletion_by_arity():
    # Initialize variables for plotting
    arity_values = list(range(2, 101))
    deletion_times_by_arity = []

    for A in arity_values:
        # Create a heap of size 10,000 with random elements for the current A value
        random_values = [random.randint(1, 100_000) for _ in range(10_001)]
        heap = AaryHeap(values=random_values, A=A)
        
        deletion_time = measure_deletion_time(heap)
        
        deletion_times_by_arity.append(deletion_time)

    plt.figure(figsize=(10, 6))
    plt.plot(arity_values, deletion_times_by_arity, linestyle='-', color='purple')
    plt.title("Deletion Time vs. Heap Arity (A Parameter)")
    plt.xlabel("Heap Arity (A Parameter)")
    plt.ylabel("Time to Delete Root Node [ms]")
    plt.xticks(range(2, 101, 10))
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    measure_insertion()
    measure_deletion()
    measure_deletion_by_arity()

