"""
Bubble Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Bubble Sort algorithm. Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The process is repeated until the list is sorted.

Parameters:
lst (List of integers): The list to be sorted.

Returns:
A list of integers sorted in ascending order.

Example:
Input: lst = [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]

Input: lst = [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
"""

def bubble_sort(arr):
    n = len(arr)

    for passes in range(0,n): # each "pass" guarantees one element reaches its correct final position (the largest unsorted element bubbles to the end).
        for j in range(0,n-1-passes):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr



unsorted_list = [12,25,11,34,90,22]
sorted_list = bubble_sort(unsorted_list)
print("Sorted Elements :", sorted_list)