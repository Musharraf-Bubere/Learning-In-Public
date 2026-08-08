# O(1) - Constant Time

numbers = [4, 8, 2, 10, 6]

first_number = numbers[0]

print(first_number)


# O(n) - Linear Time

numbers = [4, 8, 2, 10, 6]

for number in numbers:
    print(number)


# O(n²) - Quadratic Time

numbers = [1, 2, 3, 4, 5]

n = len(numbers)

for i in range(n):
    for j in range(n):
        print(i, j)