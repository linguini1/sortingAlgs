# Sorting Algorithms

## Bubble Sort
<h3>Explanation</h3>
Bubble Sort works by comparing two adjacent elements in an array. If the first element is larger than the second, they
swap places. If the first element is smaller, it remains in place. In this way, smaller elements are "bubbled" to one
end of the array, while larger elements make their way to the other. This algorithm infamously features a "temp"
variable, which stores the element being switched to avoid overwriting necessary information.

<h3>Code</h3>

<h3>Efficiency</h3>
![alt text](./graphs/Bubble%20Sort%20Efficiency.png)

## Insertion Sort
<h3>Explanation</h3>
Insertion Sort works by creating two sub-arrays of numbers, one being always in sorted order, and the other being the
remaining unsorted numbers. It moves sequentially through the array and assures that numbers are ascending. If a number
is out of place, it is moved sequentially down the array until it is in the right position.

<h3>Code</h3>

<h3>Efficiency</h3>
![alt text](./graphs/Insertion%20Sort%20Efficiency.png)

## Selection Sort
<h3>Explanation</h3>
Selection Sort iterates through an array and finds the lowest value, and moves it to the beginning of the array. Then,
it continues to search for the next lowest value and places it in the next spot closest to the front of the array. It
continues this process until the array is sorted.

<h3>Code</h3>

<h3>Efficiency</h3>
![alt text](./graphs/Selection%20Sort%20Efficiency.png)

## Quick Sort
<h3>Explanation</h3>
Quick Sort works by picking a random "pivot point" in the array (this program picks the pivot at the first array 
element), and comparing numbers on the left and right of it to see if they should be moved. Numbers smaller than the 
pivot get moved to the left side, and numbers larger than the pivot get moved to the right. Once this first step is 
complete, the array is split into two new arrays on the pivot point, and Quick Sort is recursively called on the smaller
arrays. Eventually, the algorithm returns a sorted array.

<h3>Code</h3>

<h3>Efficiency</h3>
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