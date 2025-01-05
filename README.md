# Sorting Visualizer

A Python-based graphical tool that demonstrates various sorting algorithms through real-time bar chart animations. This project helps visualize how sorting algorithms work step by step, making it an excellent educational tool for understanding sorting techniques.

---

## Features

- **Interactive Visualization**: Displays sorting progress using bar charts.
- **Algorithms Included**:
  - Bubble Sort
  - Selection Sort
  - Insertion Sort
  - Quick Sort
- **Dynamic Highlights**: Highlights the elements being compared or swapped during sorting.
- **User Input**: Allows users to choose the sorting algorithm and array size.
- **Terminal Output**: Displays the original and sorted arrays in the terminal.

---

## Requirements

### Prerequisites
Ensure you have Python 3.6+ installed on your system.  
Install the required Python libraries:

```bash
pip install matplotlib numpy
```

---

## Usage

1. Clone or download this repository.
2. Save the provided code as `sorting_visualizer.py`.
3. Run the script using the following command:

   ```bash
   python sorting_visualizer.py
   ```

4. Follow the on-screen instructions:
   - Select the sorting algorithm by entering its corresponding number.
   - Enter the number of elements to generate a random array for sorting.
   - Watch the real-time visualization of the sorting process.

---

## How It Works

### Visualization:
- **Bar Chart**: Each bar represents an element in the array.
- **Colors**: 
  - **Blue**: Unaffected elements.
  - **Red**: Elements being compared or swapped during the sorting process.
  
### Algorithms:
- **Bubble Sort**: Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
- **Selection Sort**: Finds the smallest element and places it at the beginning of the array.
- **Insertion Sort**: Builds the sorted portion of the array one element at a time.
- **Quick Sort**: Uses a pivot to partition the array into smaller subarrays and sorts them recursively.

---

## Example Run

1. **Choose an Algorithm**:
   ```
   Select Sorting Algorithm:
   1. Bubble Sort
   2. Selection Sort
   3. Insertion Sort
   4. Quick Sort
   Enter choice (1-4): 2
   ```

2. **Enter Array Size**:
   ```
   Enter number of elements: 10
   ```

3. **Output in Terminal**:
   ```
   Original Array: [45 12 89 23 34 78 90 56 10 67]
   Sorted Array: [10 12 23 34 45 56 67 78 89 90]
   ```

4. **Visualization**:
   - Watch the bar chart dynamically update as the sorting process proceeds.
