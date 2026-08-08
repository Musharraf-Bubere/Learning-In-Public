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