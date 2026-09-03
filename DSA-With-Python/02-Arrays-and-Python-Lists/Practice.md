# Practice — Arrays and Python Lists

---

## Problem 5 — Array Operations

Consider:

    numbers = [10, 20, 30, 40, 50]

### Part A — Access

    print(numbers[3])

1. What value is returned?
2. What is the time complexity?
3. Why?

### Part B — Search

    target = 50

    for number in numbers:
        if number == target:
            break

4. How many elements are checked?
5. What is the worst-case time complexity?
6. Why?

### Part C — Insertion

    numbers.insert(2, 25)

7. Which elements need to shift?
8. What is the time complexity?

### Part D — Deletion

    numbers.pop(1)

9. Which element is removed?
10. Which elements may need to shift?
11. What is the time complexity?

### Part E — Append

    numbers.append(60)

12. What is the time complexity?
13. Why?

---

## Your Answers

### Part A

    1. 40

    2. O(1)

    3. Because the element is accessed directly using its index,
       so we don't need to traverse the list.

### Part B

    4. 5 elements

    5. O(n)

    6. Because we may need to check every element using the loop.
       Therefore, in the worst case, the number of checks grows with n.

### Part C

    7. 30, 40, 50

    8. O(n)

### Part D

    9. 20

    10. 25, 30, 40, 50

    11. O(n)

### Part E

    12. O(1) amortized

    13. Appending to the end of a Python list is O(1) amortized
        because the element is normally added at the end without
        shifting existing elements.

        Occasionally, the list may need to resize its underlying
        storage, but averaged over many append operations, the
        cost is O(1).

---

## Problem 6 — Array Traversal

Consider:

    numbers = [4, 7, 2, 9, 5]

Write code to find the largest element without using max().

1. What is the largest element?
2. What is the time complexity?
3. What is the space complexity?
4. Why?

### Find Minimum

Consider:

    numbers = [10, 5, 2, 8, 3]

Write a function to find the smallest element without using min().

    def find_minimum(numbers):
        # your code

5. What is the smallest element?
6. What is the time complexity?
7. What is the space complexity?
8. Why?

### Calculate Sum

Consider:

    numbers = [10, 20, 30, 40]

Write a function to calculate the sum without using sum().

    def calculate_sum(numbers):
        # your code

9. What is the sum?
10. What is the time complexity?
11. What is the space complexity?
12. Why?

### Count Occurrences

Consider:

    numbers = [10, 20, 30, 30, 40, 30]
    target = 30

Write a function to count how many times target appears without using .count().

    def count_occurrences(numbers, target):
        # your code

13. How many times does target appear?
14. What is the time complexity?
15. What is the space complexity?
16. Why?

### Complexity Understanding

Consider:

    for number in numbers:
        if number == target:
            repeat_number += 1

17. What is the complexity of number == target?
18. What is the overall time complexity?
19. Why is the overall complexity O(n) even though the comparison itself is O(1)?

---

## Your Answers

### Find Maximum

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print(maximum)

    1. 9

    2. O(n)

    3. O(1)

    4. We traverse the list once and compare each element
       with the current maximum. Therefore, all n elements
       may need to be checked, giving O(n) time.

       We only use one extra variable, maximum, so the
       extra space complexity is O(1).

### Find Minimum

    def find_minimum(numbers):
        minimum = numbers[0]

        for number in numbers:
            if number < minimum:
                minimum = number

        return minimum

    5. 2

    6. O(n)

    7. O(1)

    8. We traverse the list once and compare each element
       with the current minimum. Therefore, the time
       complexity is O(n).

       We only maintain one extra variable, minimum,
       so the extra space complexity is O(1).

### Calculate Sum

    def calculate_sum(numbers):
        sum_numbers = 0

        for number in numbers:
            sum_numbers = sum_numbers + number

        return sum_numbers

    9. 100

    10. O(n)

    11. O(1)

    12. We traverse every element once and add each element
        to the running total. Therefore, the time complexity
        is O(n).

        We only use one extra variable, sum_numbers, so the
        extra space complexity is O(1).

### Count Occurrences

    def count_occurrences(numbers, target):
        repeat_number = 0

        for number in numbers:
            if number == target:
                repeat_number += 1

        return repeat_number

    13. 3

    14. O(n)

    15. O(1)

    16. We may need to check every element in the list,
        so the time complexity is O(n).

        We only maintain one counter variable, so the
        extra space complexity is O(1).

### Complexity Understanding

    17. O(1)

    18. O(n)

    19. The comparison number == target is O(1), but it is
        performed for every element in the list.

        Therefore:

        O(1) × n = O(n)

        So the overall time complexity is O(n).

---

## Key Takeaways

    Find Maximum:
    Traverse the list and maintain the largest value seen so far.

    Find Minimum:
    Traverse the list and maintain the smallest value seen so far.

    Calculate Sum:
    Traverse the list and maintain a running total.

    Count Occurrences:
    Traverse the list and maintain a running counter.

    General Pattern:
    Traverse once + maintain a running value → O(n) time.

    Extra Space:
    Using only a few variables → O(1) space.


## Problem 6 — Reverse an Array Using Two Pointers

### Problem

Write a function `reverse_array(numbers)` that reverses an array/list **in-place** using the two-pointer technique.

Example:

`[10, 20, 30, 40, 50]`

Expected output:

`[50, 40, 30, 20, 10]`

### Questions

1. What should the initial value of `left` be?

2. What should the initial value of `right` be?

3. Why do we use `while left < right` instead of `while left <= right`?

4. What operation is performed between `numbers[left]` and `numbers[right]`?

5. How should `left` and `right` be updated after each swap?

6. What is the time complexity of this algorithm?

7. What is the extra space complexity?

8. Why is this algorithm called an in-place algorithm?

### Your Answers

1. `left = 0`

2. `right = len(numbers) - 1`

3. We use `left < right` because when both pointers meet at the middle element, no swap is needed. The middle element is already in its correct position.

4. The elements at `left` and `right` are swapped.

5. `left` is increased by `1` and `right` is decreased by `1`.

6. Time complexity: `O(n)`

7. Extra space complexity: `O(1)`

8. It is called in-place because the original array is modified directly without creating another array.