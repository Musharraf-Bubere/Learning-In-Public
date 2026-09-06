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

## Problem 7 — Check if an Array is Sorted

### Problem

Write a function `is_sorted(numbers)` that checks whether an array/list is sorted in ascending order.

The function should:

- Return `True` if the array is sorted.
- Return `False` if the array is not sorted.
- Compare adjacent elements.
- Stop immediately when an incorrect order is found.

Example:

`[10, 20, 30, 40, 50]` → `True`

`[10, 20, 15, 40, 50]` → `False`

### Questions

1. Why do we compare `numbers[i]` with `numbers[i + 1]`?

2. Why do we use `range(len(numbers) - 1)`?

3. For ascending order, what condition tells us that the array is not sorted?

4. Why can we use `return False` immediately when an incorrect pair is found?

5. What should the function return if the entire loop finishes without finding an incorrect pair?

6. What is the best-case time complexity?

7. What is the worst-case time complexity?

8. What is the extra space complexity?

9. What happens when the input array is empty `[]`?

10. What happens when the input array contains only one element, such as `[5]`?

### Your Answers

1. We compare adjacent elements because the order of every neighboring pair determines whether the complete array is sorted.

2. We use `range(len(numbers) - 1)` because we access `numbers[i + 1]`, so `i` must stop before the last index.

3. The array is not sorted when `numbers[i] > numbers[i + 1]`.

4. We can immediately return `False` because once one adjacent pair is in the wrong order, the entire array is not sorted.

5. If the loop finishes without finding an incorrect pair, the function returns `True`.

6. Best-case time complexity: `O(1)`.

7. Worst-case time complexity: `O(n)`.

8. Extra space complexity: `O(1)`.

9. An empty array returns `True` because there are no adjacent elements that violate the sorted-order condition.

10. A single-element array returns `True` because one element is already considered sorted.

## Problem 8 — Find the Second Largest Distinct Element

### Problem

Write a function `find_second_largest(numbers)` that finds the **second-largest distinct element** in an array/list.

The function should:

- Return the second-largest distinct value.
- Use a single traversal of the array.
- Not sort the array.
- Return `None` if a second-largest distinct value does not exist.

Examples:

`[5, 10, 8, 15, 20]` → `15`

`[10, 20, 20, 5]` → `10`

`[20, 20, 20]` → `None`

`[5]` → `None`

`[]` → `None`

### Questions

1. What two values should we maintain while traversing the array?

2. Why do we initialize `largest` and `second_largest` with `None`?

3. What should happen when the current number is greater than `largest`?

4. Why does the old `largest` become `second_largest` when a new largest is found?

5. What condition should be used to prevent a duplicate of `largest` from becoming `second_largest`?

6. Why do we use `number != largest`?

7. Why is sorting unnecessary for this problem?

8. What is the time complexity of the single-pass solution?

9. What is the extra space complexity?

10. What should the function return when there is no second-largest distinct value?

11. Why should we not initialize `largest` and `second_largest` with `0`?

12. What is the result for `[-10, -5, -20, -3]`?

### Your Answers

1. We maintain `largest` and `second_largest`.

2. We initialize them with `None` to represent that no value has been found yet. It also allows the algorithm to work correctly with negative numbers.

3. The old `largest` becomes `second_largest`, and the current number becomes the new `largest`.

4. The old largest is the next-largest value after a new, larger value is found.

5. We check that the current number is different from `largest` before allowing it to become `second_largest`.

6. `number != largest` prevents a duplicate of the largest value from becoming the second-largest distinct value.

7. Sorting is unnecessary because we can find the result by maintaining `largest` and `second_largest` during a single traversal.

8. Time complexity: `O(n)`.

9. Extra space complexity: `O(1)`.

10. Return `None`.

11. Initializing with `0` can give incorrect results when the array contains negative numbers.

12. Largest = `-3`, second largest = `-5`.