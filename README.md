# Sorting Algorithms

## Bubble Sort
<h3>Explanation</h3>
Bubble Sort works by comparing two adjacent elements in an array. If the first element is larger than the second, they
swap places. If the first element is smaller, it remains in place. In this way, smaller elements are "bubbled" to one
end of the array, while larger elements make their way to the other. This algorithm infamously features a "temp"
variable, which stores the element being switched to avoid overwriting necessary information.

<h3>Code</h3>

```python
 n = len(arr)

# Traverse through all array elements
for i in range(n - 1):

    # Last i elements are already in place
    for j in range(0, n - i - 1):

        # Traverse the array from 0 to n-i-1
        # Swap if the element found is greater than the next element
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

<h3>Efficiency</h3>
This algorithm makes use of an inefficient temp variable, and uses two nested for loops. It has a complexity of O(n^2).

![alt text](./graphs/Bubble%20Sort%20Efficiency.png)

## Insertion Sort
<h3>Explanation</h3>
Insertion Sort works by creating two sub-arrays of numbers, one being always in sorted order, and the other being the
remaining unsorted numbers. It moves sequentially through the array and assures that numbers are ascending. If a number
is out of place, it is moved sequentially down the array until it is in the right position.

<h3>Code</h3>

```python
# Traverse through 1 to len(arr)
for i in range(1, len(arr)):

    key = arr[i]

    # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key
```

<h3>Efficiency</h3>
This algorithm has also uses nested loops, and is more efficient on average than Bubble Sort. Its complexity is still
O(n^2) however.

![alt text](./graphs/Insertion%20Sort%20Efficiency.png)

## Selection Sort
<h3>Explanation</h3>
Selection Sort iterates through an array and finds the lowest value, and moves it to the beginning of the array. Then,
it continues to search for the next lowest value and places it in the next spot closest to the front of the array. It
continues this process until the array is sorted.

<h3>Code</h3>

```python
for i in range(len(arr)):

    # Find the minimum element in remaining unsorted array
    min_idx = i

    for j in range(i + 1, len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j

    # Swap the found minimum element with the first element
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

<h3>Efficiency</h3>
The Selection Sort algorithm also uses nested for loops. Generally, this algorithm should perform worse than insertion
sort. It also has a complexity of O(n^2).

![alt text](./graphs/Selection%20Sort%20Efficiency.png)

## Quick Sort
<h3>Explanation</h3>
Quick Sort works by picking a random "pivot point" in the array (this program picks the pivot at the first array 
element), and comparing numbers on the left and right of it to see if they should be moved. Numbers smaller than the 
pivot get moved to the left side, and numbers larger than the pivot get moved to the right. Once this first step is 
complete, the array is split into two new arrays on the pivot point, and Quick Sort is recursively called on the smaller
arrays. Eventually, the algorithm returns a sorted array.

<h3>Code</h3>

```python
if len(arr) <= 1:
    return arr

else:
    return quick_sort([e for e in arr[1:] if e <= arr[0]]) + [arr[0]] + \
           quick_sort([e for e in arr[1:] if e > arr[0]])
```

<h3>Efficiency</h3>
Generally, Quick Sort is the most efficient of all these algorithms, and usually has a complexity of O(n log(n)) in 
average scenarios. It still has a complexity of O(n^2) in the worst case however.

![alt text](./graphs/Quick%20Sort%20Efficiency.png)

# Comparison
All the algorithms were tested by sorting an array of size x, populated with integers between 1 and 10 inclusive.

## Non-Recursive Algorithms
Here's the comparison in efficiency between the three non-recursive algorithms: Bubble Sort, Insertion Sort and
Selection Sort. Quick Sort wasn't included on this graph because it could not process over 9500 array elements without
exceeding the stack call limit, and thus did not show up on a graph of this scale.

![alt text](./graphs/Sorting%20Algorithm%20Efficiency.png)

## Recursive Algorithms
Here is a comparison in the efficiency of all the algorithms up to an array size of 9500 elements.

![alt text](./graphs/Sorting%20Algorithm%20Efficiency%20Close.png)