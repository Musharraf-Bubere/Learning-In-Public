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