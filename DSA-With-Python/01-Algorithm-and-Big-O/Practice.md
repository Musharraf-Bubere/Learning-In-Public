# Practice Problems

## Problem 1 — Find the Maximum

Given the following list:

```python
numbers = [4, 8, 2, 10, 6]
```

Find the maximum number using a loop.

### Questions

1. Write the Python solution.
2. What is the time complexity?
3. Why?

### Your Answer

```python
numbers = [4, 8, 2, 10, 6]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
```

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(1)
```

### Explanation

The algorithm checks each element in the list to find the maximum value.

If the input contains `n` elements, the loop can run `n` times.

Therefore, the time complexity is O(n).

The algorithm only uses a few variables and does not create an additional data structure that grows with the input size.

Therefore, the extra space complexity is O(1).


---

## Problem 2 — Identify the Complexity

Consider this algorithm:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

n = len(numbers)

i = 1

while i < n:
    print(i)
    i = i * 2
```

### Questions

1. How many times does the loop approximately run when `n = 8`?
2. What is the time complexity?
3. Explain why.

### Your Answer

```python
For n = 8:

i = 1 → loop
i = 2 → loop
i = 4 → loop
i = 8 → stop

The loop runs 3 times.
```

### Time Complexity

```text
O(log n)
```

### Explanation

The value of i is multiplied by 2 after every iteration:

1 → 2 → 4 → 8 → ...

Therefore, the number of iterations grows logarithmically with the input size n.

Time Complexity = O(log n)


---

## Problem 3 — Sequential vs Nested Complexity

Consider the following code:

```python
numbers = [1, 2, 3, 4, 5]

for i in range(n):
    print(i)

for j in range(n):
    for k in range(n):
        print(j, k)

for x in range(n):
    print(x)
```

### Questions

1. What is the complexity of the first loop?
2. What is the complexity of the nested loops?
3. What is the complexity of the last loop?
4. What is the overall time complexity?
5. Explain why.

### Your Answer

```text
1. First loop → O(n)
2. Nested loops → O(n²)
3. Last loop → O(n)
4. Overall → O(n²)
```

### Time Complexity

```text
O(n²)
```

### Explanation

The first and last loops are sequential O(n) operations.

The nested loops perform n × n operations, so they are O(n²).

Therefore:

O(n) + O(n²) + O(n)

The O(n²) term grows faster than O(n), so it dominates the overall complexity.

Therefore, the final time complexity is O(n²).

---

## Problem 4 — Combined Complexity

Consider:

```python
i = 1

while i < n:
    for j in range(n):
        print(i, j)

    i *= 2

for x in range(n):
    print(x)
```

### Analysis

```text
While loop → O(log n)

Inner for loop → O(n)

While + inner for:
O(log n) × O(n)
→ O(n log n)

Last for loop → O(n)
```

### Overall Time Complexity

```text
O(n log n) + O(n)
→ O(n log n)
```

### Explanation

The while loop doubles `i` on every iteration, so it runs in O(log n) time.

The inner loop processes n elements during every while-loop iteration, giving O(n log n).

The final loop runs sequentially in O(n).

Therefore:

O(n log n) + O(n)
→ O(n log n)

The O(n log n) term dominates O(n).