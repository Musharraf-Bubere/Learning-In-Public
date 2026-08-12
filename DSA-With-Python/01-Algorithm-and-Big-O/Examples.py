# # O(1) - Constant Time

# numbers = [4, 8, 2, 10, 6]

# first_number = numbers[0]

# print(first_number)


# # O(n) - Linear Time

# numbers = [4, 8, 2, 10, 6]

# for number in numbers:
#     print(number)


# # O(n²) - Quadratic Time

# numbers = [1, 2, 3, 4, 5]

# n = len(numbers)

# for i in range(n):
#     for j in range(n):
#         print(i, j)


# # O(log n) - Logarithmic Time

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# target = 7

# left = 0
# right = len(numbers) - 1

# while left <= right:
#     middle = (left + right) // 2

#     if numbers[middle] == target:
#         print("Found:", target)
#         break
#     elif numbers[middle] < target:
#         left = middle + 1
#     else:
#         right = middle - 1


# O(n log n) - Linearithmic Time

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

n = len(numbers)

levels = 0
size = n

while size > 1:
    size = size // 2
    levels += 1

for _ in range(levels):
    for number in numbers:
        print(number)