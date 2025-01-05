import matplotlib.pyplot as plt
import numpy as np
import time

# Visualization function
def visualize_sort(arr, highlight_indices=[], title="Sorting Visualization", delay=0.2):
    colors = ['red' if i in highlight_indices else 'blue' for i in range(len(arr))]
    plt.bar(range(len(arr)), arr, color=colors)
    plt.title(title)
    plt.pause(delay)
    plt.clf()

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            visualize_sort(arr, highlight_indices=[j, j+1], title="Bubble Sort")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    visualize_sort(arr, title="Bubble Sort - Sorted", delay=1.0)

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            visualize_sort(arr, highlight_indices=[i, j, min_idx], title="Selection Sort")
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    visualize_sort(arr, title="Selection Sort - Sorted", delay=1.0)

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            visualize_sort(arr, highlight_indices=[j, j+1], title="Insertion Sort")
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    visualize_sort(arr, title="Insertion Sort - Sorted", delay=1.0)

# Quick Sort visualization wrapper
def quick_sort_visual(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_visual(arr, low, pi-1)
        quick_sort_visual(arr, pi+1, high)

# Quick Sort partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        visualize_sort(arr, highlight_indices=[i, j, high], title="Quick Sort")
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

# Main function to select algorithm and display sorting
def main():
    print("Select Sorting Algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("4. Quick Sort")
    choice = int(input("Enter choice (1-4): "))

    n = int(input("Enter number of elements: "))
    arr = np.random.randint(1, 100, n)
    print(f"Original Array: {arr}")

    plt.figure(figsize=(10, 6))
    if choice == 1:
        bubble_sort(arr)
    elif choice == 2:
        selection_sort(arr)
    elif choice == 3:
        insertion_sort(arr)
    elif choice == 4:
        quick_sort_visual(arr, 0, len(arr) - 1)
        visualize_sort(arr, title="Quick Sort - Sorted", delay=1.0)
    else:
        print("Invalid choice")
        return

    plt.show()
    print(f"Sorted Array: {arr}")

if __name__ == "__main__":
    main()
