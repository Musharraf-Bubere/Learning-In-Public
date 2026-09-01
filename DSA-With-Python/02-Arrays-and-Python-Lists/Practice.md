---

## Problem 5 — Array Operations

Consider:

```python
numbers = [10, 20, 30, 40, 50]
```

### Part A — Access

```python
print(numbers[3])
```

1. What value is returned?
2. What is the time complexity?
3. Why?

### Part B — Search

```python
target = 50

for number in numbers:
    if number == target:
        break
```

4. How many elements are checked?
5. What is the worst-case time complexity?
6. Why?

### Part C — Insertion

```python
numbers.insert(2, 25)
```

7. Which elements need to shift?
8. What is the time complexity?

### Part D — Deletion

```python
numbers.pop(1)
```

9. Which element is removed?
10. Which elements may need to shift?
11. What is the time complexity?

### Part E — Append

```python
numbers.append(60)
```

12. What is the time complexity?
13. Why?

---

## Your Answers

### Part A

```text
1. 40

2. O(1)

3. Because the element is accessed directly using its index, so we don't need to traverse the list.
```

### Part B

```text
4. 5 elements

5. O(n)

6. Because we may need to check every element using the loop. Therefore, in the worst case, the number of checks grows with n.
```

### Part C

```text
7. 30, 40, 50

8. O(n)
```

### Part D

```text
9. 20

10. 25, 30, 40, 50

11. O(n)
```

### Part E

```text
12. O(1) amortized

13. Appending to the end of a Python list is O(1) amortized because the element is normally added at the end without shifting existing elements. Occasionally, the list may need to resize its underlying storage, but averaged over many append operations, the cost is O(1).
```