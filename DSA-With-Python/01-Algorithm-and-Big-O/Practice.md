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