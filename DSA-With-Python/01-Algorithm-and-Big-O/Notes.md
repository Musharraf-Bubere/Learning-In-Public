# Algorithm and Big O Analysis

## 1. What is an Algorithm?

An **algorithm** is a step-by-step procedure used to solve a problem.

### Example

Problem: Find the largest number in a list.

```python
numbers = [4, 8, 2, 10, 6]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

Output:

```text
10
```

The algorithm:

1. Start with the first number as the largest.
2. Compare each remaining number with the current largest.
3. Update the largest when a bigger number is found.
4. Continue until all elements are checked.
5. Return the largest number.

---

# 2. Why Do We Analyze Algorithms?

An algorithm can produce the correct answer but still be inefficient.

When the input becomes large, we want to know:

- How much time will the algorithm require?
- How much memory will it require?
- How does its performance change as the input grows?

This leads to **Complexity Analysis**.

---

# 3. Time Complexity

**Time Complexity** describes how the amount of work performed by an algorithm grows as the input size increases.

We usually represent the input size using:

```text
n
```

For example, if a list contains 100 elements:

```text
n = 100
```

---

# 4. Big O Notation

**Big O notation** describes the growth rate of an algorithm's resource usage as the input size grows.

It helps us compare algorithms based on scalability.

Important examples:

```text
O(1)   → Constant
O(n)   → Linear
O(n²)  → Quadratic
```

---

# 5. O(1) — Constant Time

An operation is **O(1)** when the amount of work stays roughly constant regardless of the input size.

### Example

```python
numbers = [4, 8, 2, 10, 6]

print(numbers[0])
```

Accessing an element by index takes roughly the same amount of work whether the list contains:

```text
5 elements
100 elements
1,000 elements
1,000,000 elements
```

Therefore:

```text
Time Complexity: O(1)
```

### Key idea

> Input size does not significantly affect the amount of work.

---

# 6. O(n) — Linear Time

An algorithm is **O(n)** when the amount of work grows approximately in proportion to the input size.

### Example

```python
for number in numbers:
    print(number)
```

If the list contains:

```text
5 elements    → 5 iterations
10 elements   → 10 iterations
100 elements  → 100 iterations
```

If the input contains `n` elements:

```text
n elements → n iterations
```

Therefore:

```text
Time Complexity: O(n)
```

### Key idea

> As `n` increases, the work increases approximately linearly.

---

# 7. Sequential Loops

Consider:

```python
for number in numbers:
    print(number)

for number in numbers:
    print(number)
```

Each loop runs `n` times.

Total:

```text
n + n = 2n
```

Initially we can write:

```text
O(2n)
```

But Big O ignores constant factors:

```text
O(2n) → O(n)
```

Therefore:

```text
Time Complexity: O(n)
```

### Important

Two separate loops do **not** automatically mean `O(n²)`.

Sequential loops usually add:

```text
O(n) + O(n) = O(n)
```

after removing constant factors.

---

# 8. O(n²) — Quadratic Time

An algorithm is **O(n²)** when work grows approximately with the square of the input size.

### Example

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

The outer loop runs `n` times.

For every outer iteration, the inner loop also runs `n` times.

Therefore:

```text
n × n = n²
```

So:

```text
Time Complexity: O(n²)
```

### Example

If:

```text
n = 5
```

then:

```text
5 × 5 = 25
```

The `print()` statement executes 25 times.

If:

```text
n = 100
```

then:

```text
100 × 100 = 10,000
```

---

# 9. Nested Loops Are Not Always O(n²)

Do not assume:

> "Nested loop = O(n²)"

Always check what each loop depends on.

### Example

```python
for i in range(n):
    for j in range(5):
        print(i, j)
```

The outer loop runs `n` times.

The inner loop always runs 5 times.

Therefore:

```text
n × 5 = 5n
```

Remove the constant:

```text
O(5n) → O(n)
```

Therefore:

```text
Time Complexity: O(n)
```

### Important rule

> Analyze how the number of operations grows with `n`, not simply how many loops appear in the code.

---

# 10. Common Complexity Patterns

| Code Pattern | Time Complexity |
|---|---|
| Direct access such as `numbers[0]` | O(1) |
| One loop depending on `n` | O(n) |
| Two separate loops depending on `n` | O(n) |
| Nested loops both depending on `n` | O(n²) |
| Nested loop with a constant inner loop | O(n) |

---

# 11. O(n) vs O(n²)

### O(n)

Linear growth:

```text
n → n
```

### O(n²)

Quadratic growth:

```text
n → n²
```

Example:

| Input `n` | O(n) | O(n²) |
|---:|---:|---:|
| 10 | 10 | 100 |
| 100 | 100 | 10,000 |
| 1,000 | 1,000 | 1,000,000 |

As the input becomes large, `O(n²)` grows much faster than `O(n)`.

---

# 12. Most Important Mindset

Do not determine complexity only by counting loops.

Instead ask:

> **How does the number of operations grow when the input size `n` grows?**

For example:

```python
for i in range(n):
    ...
```

→ `O(n)`

```python
for i in range(n):
    for j in range(n):
        ...
```

→ `O(n²)`

```python
for i in range(n):
    for j in range(5):
        ...
```

→ `O(n)`

---

# 13. Quick Revision

### O(1)

Constant time.

```python
numbers[0]
```

---

### O(n)

Linear time.

```python
for number in numbers:
    print(number)
```

---

### O(n²)

Quadratic time.

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

---

# 14. Key Takeaways

- An algorithm is a step-by-step procedure for solving a problem.
- Time complexity describes how algorithmic work grows with input size.
- Big O notation is used to describe growth rate.
- `O(1)` → constant growth.
- `O(n)` → linear growth.
- `O(n²)` → quadratic growth.
- Sequential `O(n)` loops remain `O(n)`.
- Nested loops are not automatically `O(n²)`.
- Always examine how each loop depends on `n`.
- Constant factors are ignored in Big O notation.

---

# 15. What We Have Learned

```text
O(1)   → Constant
O(n)   → Linear
O(n²)  → Quadratic
```

These are the first building blocks of complexity analysis.

---

# 16. Next

Next we will continue with **Big O Analysis** and learn more important complexity patterns before moving to Arrays.

We will not move forward until these fundamentals are comfortable.