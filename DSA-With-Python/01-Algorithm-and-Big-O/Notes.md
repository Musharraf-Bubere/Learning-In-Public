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

---

# Day 2 — Additional Big O Complexity

## 17. O(log n) — Logarithmic Time

An algorithm is **O(log n)** when the amount of work grows logarithmically as the input size increases.

A common pattern is repeatedly reducing the search space by half.

### Example

Suppose we have a sorted list:

```text
[1, 2, 3, 4, 5, 6, 7, 8]
```

We want to find `7`.

Instead of checking every element one by one, we can look at the middle:

```text
[1, 2, 3, 4] | [5, 6, 7, 8]
```

Since `7` is greater than the middle value, we can ignore the left half.

The search space becomes smaller:

```text
8 elements
↓
4 elements
↓
2 elements
↓
1 element
```

The search space is repeatedly divided by 2.

Therefore:

```text
Time Complexity: O(log n)
```

### Important Idea

> **O(log n) → repeatedly reduce the problem size, typically by half.**

---

## 18. Understanding O(log n)

For example:

```text
n = 16

16
↓
8
↓
4
↓
2
↓
1
```

It takes 4 halvings.

Therefore:

```text
log₂(16) = 4
```

Another example:

```text
n = 32

32
↓
16
↓
8
↓
4
↓
2
↓
1
```

It takes 5 halvings.

Therefore:

```text
log₂(32) = 5
```

The important idea is not memorizing the calculation.

The important pattern is:

```text
n → n/2 → n/4 → n/8 → ...
```

---

# 19. O(n log n) — Linearithmic Time

An algorithm can have:

- `n` amount of work
- repeated across `log n` levels

Therefore:

```text
n × log n
```

gives:

```text
O(n log n)
```

### Example

Suppose an algorithm processes `n` elements at each of `log n` levels.

If:

```text
n = 8
```

then:

```text
log₂(8) = 3
```

The work can be viewed as:

```text
Level 1 → 8 operations
Level 2 → 8 operations
Level 3 → 8 operations
```

Total:

```text
8 + 8 + 8
= 8 × 3
= 24
```

Therefore:

```text
O(n log n)
```

### Important Idea

> **O(n log n) → n work performed across log n levels.**

This complexity commonly appears in efficient sorting algorithms such as Merge Sort.

---

# 20. O(log n) vs O(n log n)

### O(log n)

The algorithm mainly reduces the problem size repeatedly.

```text
n
↓
n/2
↓
n/4
↓
n/8
↓
...
```

Example:

```text
Binary Search
```

Typical complexity:

```text
O(log n)
```

---

### O(n log n)

The algorithm performs `n` amount of work at each logarithmic level.

```text
n work
×
log n levels
```

Therefore:

```text
O(n log n)
```

---

# 21. Complexity Growth Order

For large input sizes, the following complexities generally grow from slower to faster:

```text
O(1)
↓
O(log n)
↓
O(n)
↓
O(n log n)
↓
O(n²)
```

This means an algorithm with `O(log n)` generally scales much better than one with `O(n)` for very large inputs.

Similarly, `O(n)` generally scales better than `O(n log n)`, which generally scales better than `O(n²)`.

---

# 22. Complexity Patterns Learned So Far

| Complexity | Name | Main Idea |
|---|---|---|
| O(1) | Constant | Direct/constant amount of work |
| O(log n) | Logarithmic | Repeatedly reduce the problem size |
| O(n) | Linear | Process input elements proportionally to n |
| O(n log n) | Linearithmic | n work across log n levels |
| O(n²) | Quadratic | n work repeated n times |

---

# 23. Mental Models

Instead of memorizing formulas, recognize these patterns:

```text
O(1)
→ Direct access / constant work
```

```text
O(log n)
→ Keep cutting the search space
```

```text
O(n)
→ Go through the input
```

```text
O(n log n)
→ Process n elements across log n levels
```

```text
O(n²)
→ Compare/process n elements against n elements
```

---

# 24. Important Reminder

Do not determine complexity only by counting loops.

Always ask:

> **How does the amount of work grow as the input size `n` grows?**

For example:

```python
for i in range(n):
    ...
```

→ `O(n)`

While:

```python
for i in range(n):
    for j in range(n):
        ...
```

→ `O(n²)`

And an algorithm that repeatedly halves its search space:

```text
n → n/2 → n/4 → n/8 → ...
```

→ `O(log n)`

---

# 25. Day 2 Key Takeaways

- `n` represents the input size.
- `O(log n)` grows logarithmically.
- A common `O(log n)` pattern is repeatedly cutting the search space in half.
- Binary Search is a classic example of `O(log n)`.
- `O(n log n)` combines linear work with logarithmic levels.
- Merge Sort is a common example of `O(n log n)`.
- `O(log n)` generally grows much more slowly than `O(n)`.
- `O(n log n)` generally grows faster than `O(n)` but slower than `O(n²)`.
- Always analyze how the number of operations grows with `n`.

---

# 26. Complexity Summary

```text
O(1)
Constant

O(log n)
Logarithmic

O(n)
Linear

O(n log n)
Linearithmic

O(n²)
Quadratic
```

These complexity classes form an important foundation for understanding the efficiency of algorithms.


---

# Day 3 — Combining Big O Complexities

## 27. Sequential Operations

When operations happen one after another, we **add** their complexities.

Example:

```python
print(numbers[0])

for number in numbers:
    print(number)
```

Complexity:

```text
O(1) + O(n)
```

The dominant term is `O(n)`:

```text
O(1) + O(n) → O(n)
```

Therefore:

```text
Overall: O(n)
```

---

## 28. Multiple Sequential Loops

Example:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Each loop is:

```text
O(n)
```

Therefore:

```text
O(n) + O(n)
= O(2n)
= O(n)
```

### Key Rule

> **Sequential operations → Add their complexities.**

---

## 29. Nested Operations

When one operation is performed inside another, their work is multiplied.

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Outer loop:

```text
O(n)
```

Inner loop:

```text
O(n)
```

Because the inner loop runs `n` times for every outer iteration:

```text
n × n = n²
```

Therefore:

```text
O(n²)
```

### Key Rule

> **Nested operations → Multiply their complexities.**

---

## 30. Sequential + Nested Operations

Consider:

```python
for i in range(n):
    print(i)

for j in range(n):
    for k in range(n):
        print(j, k)

for x in range(n):
    print(x)
```

Break it into parts:

```text
First loop       → O(n)

Nested loops     → O(n²)

Last loop        → O(n)
```

Since the operations are sequential:

```text
O(n) + O(n²) + O(n)
```

The dominant term is `O(n²)`:

```text
O(n) + O(n²) + O(n)
→ O(n²)
```

Therefore:

```text
Overall Time Complexity: O(n²)
```

---

## 31. Dominant Term

When adding different complexity terms, keep the term that grows the fastest.

Examples:

```text
O(1) + O(n)
→ O(n)
```

```text
O(n) + O(n)
→ O(n)
```

```text
O(n) + O(n²)
→ O(n²)
```

```text
O(n) + O(n²) + O(n³)
→ O(n³)
```

### Important Idea

> The fastest-growing term dominates the overall complexity.

---

## 32. Sequential vs Nested

### Sequential

```python
for i in range(n):
    ...

for j in range(n):
    ...
```

```text
O(n) + O(n)
→ O(n)
```

### Nested

```python
for i in range(n):
    for j in range(n):
        ...
```

```text
O(n) × O(n)
→ O(n²)
```

---

## 33. Mental Model

Remember:

```text
Sequential
↓
ADD
↓
O(n) + O(n)
↓
O(n)
```

```text
Nested
↓
MULTIPLY
↓
O(n) × O(n)
↓
O(n²)
```

And:

```text
Different sequential complexities
↓
ADD
↓
Keep the dominant term
```

Example:

```text
O(n) + O(n²)
↓
O(n²)
```

---

# 34. Day 3 Key Takeaways

- Sequential operations are added.
- Nested operations are multiplied.
- Constant factors are ignored.
- When different complexity terms are added, the dominant term remains.
- `O(n) + O(n)` → `O(n)`
- `O(n) + O(n²)` → `O(n²)`
- `O(n) × O(n)` → `O(n²)`
- Always analyze the structure of the code instead of simply counting loops.

---

# 35. Big O So Far

```text
O(1)
↓
Constant

O(log n)
↓
Logarithmic

O(n)
↓
Linear

O(n log n)
↓
Linearithmic

O(n²)
↓
Quadratic
```

### Combination Rules

```text
Sequential → ADD

Nested → MULTIPLY

Different terms → Keep the dominant term
```

---

# Day 4 — Combining Big O in Real Code

## 36. Analyzing Complex Code Step by Step

When code contains multiple loops and operations, don't try to determine the overall complexity immediately.

Use this process:

```text
1. Analyze each part separately
2. Identify sequential operations
3. Identify nested operations
4. Add sequential complexities
5. Multiply nested complexities
6. Remove constant factors
7. Keep the dominant term
```

---

## 37. Sequential Operations

When operations happen one after another, add their complexities.

Example:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Analysis:

```text
O(n) + O(n)
= O(2n)
= O(n)
```

Therefore:

```text
Overall → O(n)
```

---

## 38. Nested Operations

When one loop is inside another, multiply their complexities.

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Analysis:

```text
O(n) × O(n)
= O(n²)
```

Therefore:

```text
Overall → O(n²)
```

---

## 39. Logarithmic Loop

A loop where the variable doubles each iteration:

```python
i = 1

while i < n:
    print(i)
    i *= 2
```

has:

```text
O(log n)
```

because:

```text
1 → 2 → 4 → 8 → 16 → ...
```

The number of iterations grows logarithmically.

---

## 40. O(n log n) from Nested Complexity

Consider:

```python
i = 1

while i < n:
    for j in range(n):
        print(i, j)

    i *= 2
```

Analysis:

```text
while loop → O(log n)

inner loop → O(n)
```

The inner loop runs during every iteration of the while loop:

```text
O(log n) × O(n)
= O(n log n)
```

Therefore:

```text
Overall → O(n log n)
```

---

## 41. Combining O(n log n) and O(n)

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

First section:

```text
O(n log n)
```

Second section:

```text
O(n)
```

They are sequential:

```text
O(n log n) + O(n)
```

The dominant term is:

```text
O(n log n)
```

Therefore:

```text
Overall → O(n log n)
```

---

## 42. Common Mistakes

### Mistake 1 — Assuming every loop is O(n²)

This:

```python
for i in range(n):
    print(i)
```

is:

```text
O(n)
```

Not O(n²).

---

### Mistake 2 — Multiplying sequential loops

This:

```python
for i in range(n):
    ...

for j in range(n):
    ...
```

is:

```text
O(n) + O(n)
→ O(n)
```

Not:

```text
O(n²)
```

---

### Mistake 3 — Ignoring the dominant term

```text
O(n) + O(n²)
```

becomes:

```text
O(n²)
```

because O(n²) grows faster.

---

### Mistake 4 — Confusing O(log n) and O(n log n)

```text
O(log n)
→ logarithmic number of operations
```

while:

```text
O(n log n)
→ n operations at each logarithmic level
```

---

# 43. Big O Analysis Checklist

When you see an algorithm, ask:

### Question 1

Does it access something directly?

```text
→ O(1)
```

### Question 2

Does it process each element?

```text
→ O(n)
```

### Question 3

Does the problem size repeatedly get divided?

```text
→ O(log n)
```

### Question 4

Are operations nested?

```text
→ Multiply
```

### Question 5

Are operations sequential?

```text
→ Add
```

### Question 6

Are there different complexity terms?

```text
→ Keep the dominant term
```

---

# 44. Day 4 Key Takeaways

The most important skill from today is not memorizing more Big O values.

It is learning how to **analyze an algorithm step by step**.

Remember:

```text
Sequential → ADD
Nested → MULTIPLY
Dominant term → KEEP
```

Examples:

```text
O(1) + O(n)
→ O(n)
```

```text
O(n) + O(n)
→ O(n)
```

```text
O(n) + O(n²)
→ O(n²)
```

```text
O(log n) × O(n)
→ O(n log n)
```

```text
O(n) × O(n)
→ O(n²)
```

---

# 45. Big O Foundation Complete

So far we have learned:

```text
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
```

We can now analyze simple combinations of these complexities.

This forms the foundation we need before moving into data structures.

---

# 🚀 Next Topic

The next major topic is:

```text
Arrays / Python Lists
```

We will learn:

```text
Array
↓
Python List
↓
Indexing
↓
Traversal
↓
Searching
↓
Insertion
↓
Deletion
↓
Complexities
↓
Practice
```

We will connect every operation back to Big O.