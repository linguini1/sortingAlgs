# Bubble sort algorithm

# Imports
import random
import time
import math

# Getting user input

# Which sorting algorithm
while True:
    algorithm = input("Use bubble sort (1), insertion sort (2), selection sort (3), or quick sort (4): ")

    # Invalid selection
    if algorithm not in ['1', '2', '3', '4']:
        print("You must pick option 1, 2, 3 or 4.")

    # Selected successfully
    else:
        break

# Array size
while True:

    arraySize = input("Number of integers the array will store: ")

    # Converting to int
    try:
        arraySize = int(arraySize)

        # Array must be greater than 1
        if arraySize <= 1:
            print("Your array must store more than two numbers.")

        # Quicksort exceeds the stack limit with arrays over 9000 elements, so the number must be lower than that
        else:
            if arraySize > 9000 and algorithm == "4":
                print("If you selected quicksort, your array cannot be longer than 9000 elements.")
            else:
                break

    except ValueError:
        print("You didn't input a valid integer size.")

# Integers or floats
while True:
    integers = input("Use integer elements (1) or float elements (2): ")

    if integers == "1":  # Integers
        integers = True
        break

    elif integers == "2":  # Floats
        integers = False
        break

    else:  # Bad input
        print("Invalid selection.")

# Getting range for random numbers
while True:

    numRange = input("The range for the random numbers in format 'x-y': ")

    # Splitting input
    numRange = numRange.split("-")

    # Making sure there's exactly two numbers
    if len(numRange) != 2:
        print("Invalid input, try again!")

    # Checking to make sure they convert to numbers
    else:

        if integers:
            try:
                minRange = min(int(numRange[0]), int(numRange[1]))
                maxRange = max(int(numRange[0]), int(numRange[1]))
                break
            except ValueError:
                print("You didn't give a valid integer!")

        else:
            try:
                minRange = min(float(numRange[0]), float(numRange[1]))
                maxRange = max(float(numRange[0]), float(numRange[1]))
                break
            except ValueError:
                print("You didn't give a valid float!")


# Factor
def factor_int(n):
    a = math.floor(math.sqrt(n))
    b = math.ceil(n / float(a))
    return a, b


# Displaying array
def array_display(arr):

    # Determine the factor closest to the square of the number to print array in a reasonable rectangle
    greatestFactor = factor_int(len(arr))[0]

    # Making the array fit on screen if the square width is too large
    if integers and greatestFactor > 50:
        greatestFactor = 50

    elif not integers and greatestFactor > 11:
        greatestFactor = 11

    # Printing array
    for index, _ in enumerate(arr):

        _ = str(_)  # Converting to string for zero padding

        if index % greatestFactor == 0:  # When we've completed a row, make a new line
            print()

        if integers:  # Integers
            print(f"{_.zfill(len(str(maxRange)))} ", end="")  # Zero pad based on length of max value, no line break

        else:  # Floats
            # Decimals are maximum 18 characters long, including the period
            print(f"{_.zfill(18)} ", end="")


# Bubble sort algorithm
def bubble_sort(arr):

    t1 = time.time()  # Start time

    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    t2 = time.time()  # End time

    return arr, t2 - t1


# Insertion sort algorithm
def insertion_sort(arr):

    t1 = time.time()  # Start time

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    t2 = time.time()  # End time

    return arr, t2 - t1


# Selection sort algorithm
def selection_sort(arr):

    t1 = time.time()  # Start time

    for i in range(len(arr)):

        # Find the minimum element in remaining unsorted array
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    t2 = time.time()  # End time

    return arr, t2 - t1


# Quick sort algorithm
def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    else:
        return quick_sort([e for e in arr[1:] if e <= arr[0]]) + [arr[0]] + \
               quick_sort([e for e in arr[1:] if e > arr[0]])


# Filling an array
if integers:  # Integer array
    randNums = [random.randint(minRange, maxRange) for _ in range(arraySize)]

else:  # Float Array
    randNums = [random.uniform(minRange, maxRange) for _ in range(arraySize)]

# Printing original array
print()
print("-----ORIGINAL ARRAY-----")
array_display(randNums)
print("\n\n")

# Performing sort
if algorithm == "1":  # Bubble
    sortedArr, sortTime = bubble_sort(randNums)

elif algorithm == "2":  # Insertion
    sortedArr, sortTime = insertion_sort(randNums)

elif algorithm == "3":  # Selection
    sortedArr, sortTime = selection_sort(randNums)

else:  # Quick
    start = time.time()  # Start time
    sortedArr = quick_sort(randNums)
    end = time.time()  # End time
    sortTime = end - start

# Printing sorted array
print("-----SORTED ARRAY-----")
array_display(sortedArr)
print("\n\n")

# Displaying information
algorithms = {"1": "Bubble",
              "2": "Insertion",
              "3": "Selection",
              "4": "Quick"}  # Sort type for display

print(f"{algorithms[algorithm]} Sort sorted an array of size {arraySize} in {sortTime}s.")
