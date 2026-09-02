# Arrays and Python Lists

## Day 5 — Introduction to Arrays and Python Lists

### 1. What is an Array?

An array is a data structure that stores multiple elements in an ordered collection.

Elements are associated with positions called indexes.

Example:

```text
Index:    0    1    2    3    4
          ↓    ↓    ↓    ↓    ↓
Values:  10   20   30   40   50
```

Indexes usually start from `0`.

---

## 2. Python Lists

Python provides a built-in `list` type that is commonly used for array-like data.

Example:

```python
numbers = [10, 20, 30, 40, 50]
```

For our DSA practice, Python lists will be used extensively to implement and understand array-based algorithms.

Important distinction:

> An array is a data structure concept, while Python's `list` is a built-in data type with dynamic behavior and array-like indexing.

---

# 3. Accessing an Element

Elements can be accessed directly using their index.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[3])
```

Output:

```text
40
```

Because the index is directly used:

```text
numbers[3]
```

the operation is:

```text
Time Complexity: O(1)
```

### Key Idea

> Accessing an element by index is constant time.

---

# 4. Traversal

Traversal means visiting every element in the list.

Example:

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)
```

Every element is processed.

If:

```text
n = 5
```

there are 5 iterations.

If:

```text
n = 1000
```

there are approximately 1000 iterations.

Therefore:

```text
Time Complexity: O(n)
```

### Key Idea

> Traversal processes elements proportionally to the input size.

---

# 5. Linear Search

Linear Search checks elements one by one until the target is found.

Example:

```python
numbers = [10, 20, 30, 40, 50]

target = 40

for number in numbers:
    if number == target:
        print("Found:", target)
        break
```

The search progresses like:

```text
10 → 20 → 30 → 40
              ↑
            found
```

### Worst Case

If the target is at the end:

```text
10 → 20 → 30 → 40 → 50
```

all elements are checked.

If the target doesn't exist, all elements are also checked.

Therefore:

```text
Linear Search
Best Case  → O(1)
Worst Case → O(n)
```

When we generally describe Linear Search complexity, we use:

```text
O(n)
```

because we usually focus on the worst case.

---

# 6. Linear Search Using a Function

A reusable implementation:

```python
def linear_search(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False
```

Usage:

```python
numbers = [10, 20, 30, 40, 50]

print(linear_search(numbers, 40))
print(linear_search(numbers, 100))
```

Output:

```text
True
False
```

The worst-case complexity remains:

```text
O(n)
```

---

# 7. Python For-Else with Linear Search

Python's `for` loop can have an `else` block.

Example:

```python
numbers = [10, 20, 30, 40, 50]

target = 100

for number in numbers:
    if number == target:
        print("Found:", target)
        break
else:
    print("Not found")
```

The `else` block executes when the loop finishes without encountering `break`.

Therefore:

```text
Target found
→ break
→ for-else skipped

Target not found
→ loop finishes
→ else executes
```

---

# 8. Insertion

Insertion means adding an element to a specific position.

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers.insert(2, 25)
```

Result:

```text
[10, 20, 25, 30, 40, 50]
```

To make room for `25`, elements after the insertion position may need to shift:

```text
30 → right
40 → right
50 → right
```

Therefore, insertion at the beginning or middle is generally:

```text
O(n)
```

---

# 9. Append

Appending means adding an element to the end of a Python list.

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers.append(60)
```

Result:

```text
[10, 20, 30, 40, 50, 60]
```

Appending to the end of a Python list is:

```text
O(1) amortized
```

### What does amortized mean?

Most individual appends are constant time, although occasionally Python may need to resize its underlying storage.

When averaged across many append operations:

```text
append → O(1) amortized
```

For now, remember the complexity rather than worrying about the internal memory implementation.

---

# 10. Deletion

An element can be removed using `pop()`.

Example:

```python
numbers = [10, 20, 30, 40, 50]

numbers.pop(2)
```

Result:

```text
[10, 20, 40, 50]
```

When an element is removed from the beginning or middle, elements after it may need to shift left.

Therefore:

```text
Delete from beginning/middle → O(n)
```

---

# 11. Removing the Last Element

Removing the last element is different.

```python
numbers.pop()
```

The last element can be removed without shifting the remaining elements.

Therefore:

```text
pop() from end → O(1)
```

---

# 12. Array/List Operation Complexity

| Operation | Complexity |
|---|---:|
| Access by index | O(1) |
| Traversal | O(n) |
| Linear Search — Best Case | O(1) |
| Linear Search — Worst Case | O(n) |
| Insert at beginning/middle | O(n) |
| Append at end | O(1) amortized |
| Delete at beginning/middle | O(n) |
| `pop()` from end | O(1) |

---

# 13. Important Mental Model

Think about what the operation needs to do.

### Direct access

```text
Give me index 3
↓
Directly access it
↓
O(1)
```

### Traversal

```text
Visit every element
↓
O(n)
```

### Linear Search

```text
Check elements one by one
↓
O(n) worst case
```

### Insertion in the middle

```text
Make space
↓
Shift elements
↓
O(n)
```

### Deletion in the middle

```text
Remove element
↓
Shift remaining elements
↓
O(n)
```

### Append

```text
Add to end
↓
O(1) amortized
```

---

# 14. Day 5 Key Takeaways

- Arrays store elements in an ordered collection.
- Indexes allow direct access to elements.
- Python lists are commonly used for array-like DSA problems.
- Index access is `O(1)`.
- Traversal is `O(n)`.
- Linear Search is `O(n)` in the worst case.
- Linear Search has a best case of `O(1)`.
- Insertion at the beginning or middle is generally `O(n)`.
- Appending to the end of a Python list is `O(1)` amortized.
- Deleting from the beginning or middle is generally `O(n)`.
- `pop()` from the end is `O(1)`.
- Shifting elements is the main reason insertion and deletion can be `O(n)`.

---

# 15. Big O Connection

Our previous Big O knowledge now connects directly to arrays:

```text
Array Access
→ O(1)

Array Traversal
→ O(n)

Linear Search
→ O(n)

Insertion
→ O(n)

Deletion
→ O(n)
```

This is the beginning of understanding **why different data structures are useful for different operations**.

---

## Day 6 — Array Traversal Patterns

Today we practiced common array traversal problems using Python lists.

The main idea is:

> Traverse the list once and maintain a running value.

These patterns are extremely common in DSA.

---

# 16. Finding the Maximum Element

To find the largest element, start by assuming the first element is the maximum.

Then traverse the list and update the maximum whenever a larger element is found.

Example:

    numbers = [4, 7, 2, 9, 5]

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

    print(maximum)

Output:

    9

The algorithm checks each element and keeps track of the largest value seen so far.

### Complexity

    Time Complexity: O(n)

    Space Complexity: O(1)

Why?

There are n elements, so we may need to examine every element.

Only one additional variable, maximum, is used.

---

# 17. Finding the Minimum Element

Finding the minimum uses the same pattern as finding the maximum.

The difference is that we check whether the current element is smaller.

Example:

    numbers = [10, 5, 2, 8, 3]

    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    print(minimum)

Output:

    2

### Reusable Function

    def find_minimum(numbers):
        minimum = numbers[0]

        for number in numbers:
            if number < minimum:
                minimum = number

        return minimum

### Complexity

    Time Complexity: O(n)

    Space Complexity: O(1)

---

# 18. Calculating the Sum

To calculate the sum of all elements, maintain a running total.

Start the total at 0.

Example:

    numbers = [10, 20, 30, 40]

    sum_numbers = 0

    for number in numbers:
        sum_numbers = sum_numbers + number

    print(sum_numbers)

Output:

    100

### Reusable Function

    def calculate_sum(numbers):
        sum_numbers = 0

        for number in numbers:
            sum_numbers = sum_numbers + number

        return sum_numbers

### Complexity

    Time Complexity: O(n)

    Space Complexity: O(1)

Why?

Every element must be visited once.

Only one additional variable is used to store the running total.

---

# 19. Counting Occurrences

Counting occurrences means finding how many times a target value appears in a list.

Example:

    numbers = [10, 20, 30, 30, 40, 30]

    target = 30

    repeat_number = 0

    for number in numbers:
        if number == target:
            repeat_number += 1

    print(repeat_number)

Output:

    3

### Reusable Function

    def count_occurrences(numbers, target):
        repeat_number = 0

        for number in numbers:
            if number == target:
                repeat_number += 1

        return repeat_number

### Complexity

    Time Complexity: O(n)

    Space Complexity: O(1)

Why?

The algorithm may need to check every element, even if the target is found multiple times.

The comparison itself is O(1), but it is performed n times.

Therefore:

    O(1) × n = O(n)

---

# 20. The Running Value Pattern

The problems we solved today follow a common pattern.

The general structure is:

    running_value = initial_value

    for element in numbers:
        # update running_value

    return running_value

Different problems use different running values.

| Problem | Running Value | Update Rule |
|---|---|---|
| Find Maximum | `maximum` | Update if current element is larger |
| Find Minimum | `minimum` | Update if current element is smaller |
| Calculate Sum | `sum_numbers` | Add current element |
| Count Occurrences | `repeat_number` | Increase when target is found |

This pattern is one of the most important basic array traversal techniques.

---

# 21. Why These Algorithms Are O(n)

Consider:

    for number in numbers:
        if number == target:
            repeat_number += 1

The comparison:

    number == target

takes constant time:

    O(1)

However, the loop may execute once for every element.

If the list contains n elements:

    O(1) × n = O(n)

Therefore:

    Overall Time Complexity = O(n)

### Important Rule

> A single traversal through n elements is generally O(n).

---

# 22. Maximum and Minimum Pattern

Maximum and minimum problems are almost identical.

### Maximum

    maximum = numbers[0]

    for number in numbers:
        if number > maximum:
            maximum = number

### Minimum

    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

The main difference is the comparison operator:

    Maximum → >

    Minimum → <

---

# 23. Running Counter Pattern

Counting problems commonly use a counter.

Example:

    count = 0

    for number in numbers:
        if condition:
            count += 1

    return count

This pattern can be used for:

- Counting occurrences
- Counting positive numbers
- Counting negative numbers
- Counting even numbers
- Counting elements satisfying a condition

The traversal is usually:

    Time Complexity: O(n)

And if only a counter is used:

    Space Complexity: O(1)

---

# 24. Running Sum Pattern

The running sum pattern maintains a total while traversing.

Example:

    total = 0

    for number in numbers:
        total += number

    return total

The important idea is:

> Do not repeatedly calculate the entire sum. Build the result while traversing.

Complexity:

    Time Complexity: O(n)

    Space Complexity: O(1)

---

# 25. Important Mental Model

When given an array problem, ask:

    1. Do I need to visit every element?

    2. What information do I need to maintain while traversing?

    3. What should the initial value be?

    4. How should I update that value?

    5. What should I return after the loop?

For example:

    Find maximum
    → maintain maximum

    Find minimum
    → maintain minimum

    Find sum
    → maintain total

    Count elements
    → maintain counter

---

# 26. Day 6 Key Takeaways

- Array traversal means visiting elements one by one.

- A single complete traversal is generally O(n).

- Finding the maximum can be solved using a running maximum.

- Finding the minimum can be solved using a running minimum.

- Sum problems can be solved using a running total.

- Counting problems can be solved using a running counter.

- These algorithms usually require O(1) extra space when only a few variables are used.

- An O(1) operation inside an O(n) loop results in O(n) overall time.

- Maximum and minimum use almost identical logic.

- The running value pattern is a fundamental DSA technique.

---

# 27. Connection With Previous Big O Knowledge

Our Big O concepts now directly apply to array problems.

    Direct index access
    → O(1)

    Single traversal
    → O(n)

    Linear search
    → O(n) worst case

    Find maximum
    → O(n)

    Find minimum
    → O(n)

    Calculate sum
    → O(n)

    Count occurrences
    → O(n)

The key skill is no longer just memorizing Big O.

We are now learning to:

    Look at the code
    ↓
    Understand how many times operations execute
    ↓
    Determine the complexity

This is the foundation for analyzing more advanced DSA algorithms.