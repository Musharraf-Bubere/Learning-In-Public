# Linear Search

# numbers = [10, 20, 30, 40, 50]

# target = 40

# for number in numbers:
#     if number == target:
#         print("Found:", target)
#         break
# else:
#     print("Not found")


# Linear Search Using Function

# def linear_search(numbers, target):
#     for number in numbers:
#         if number == target:
#             return True
#     return False


# numbers = [10, 20, 30, 40, 50]

# print(linear_search(numbers, 40))
# print(linear_search(numbers, 100))


# Insertion

# numbers = [10, 20, 30, 40, 50]

# numbers.insert(2, 25)

# print(numbers)


# Array Traversal — Find Maximum

# numbers = [4, 7, 2, 9, 5]

# maximum = numbers[0]

# for number in numbers:
#     if number > maximum:
#         maximum = number

# print("Maximum:", maximum)


# # Array Traversal — Find Minimum

# numbers = [10, 5, 2, 8, 3]

# minimum = numbers[0]

# for number in numbers:
#     if number < minimum:
#         minimum = number

# print("Minimum:", minimum)


# # Array Traversal — Calculate Sum

# numbers = [10, 20, 30, 40]

# sum_numbers = 0

# for number in numbers:
#     sum_numbers = sum_numbers + number

# print("Sum:", sum_numbers)


# # Array Traversal — Count Occurrences

# numbers = [10, 20, 30, 30, 40, 30]

# target = 30

# repeat_number = 0

# for number in numbers:
#     if number == target:
#         repeat_number += 1

# print("Occurrences:", repeat_number)


# # Find Minimum Using Function

# def find_minimum(numbers):
#     minimum = numbers[0]

#     for number in numbers:
#         if number < minimum:
#             minimum = number

#     return minimum


# numbers = [10, 5, 2, 8, 3]

# print("Function Minimum:", find_minimum(numbers))


# # Calculate Sum Using Function

# def calculate_sum(numbers):
#     sum_numbers = 0

#     for number in numbers:
#         sum_numbers = sum_numbers + number

#     return sum_numbers


# numbers = [10, 20, 30, 40]

# print("Function Sum:", calculate_sum(numbers))


# # Count Occurrences Using Function

# def count_occurrences(numbers, target):
#     repeat_number = 0

#     for number in numbers:
#         if number == target:
#             repeat_number += 1

#     return repeat_number


# numbers = [10, 20, 30, 30, 40, 30]

# print("Function Occurrences:", count_occurrences(numbers, 30))

# ============================================================
# Day 7 — Reverse an Array Using Two Pointers
# ============================================================

def reverse_array(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]

        left += 1
        right -= 1

    return numbers


# Example
numbers = [10, 20, 30, 40, 50]

print(reverse_array(numbers))

# Output:
# [50, 40, 30, 20, 10]

# ============================================================
# Day 8 — Check if an Array is Sorted
# ============================================================

# Ascending Order
def is_sorted_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


numbers = [10, 20, 30, 40, 50]

print(is_sorted_ascending(numbers))

# Output:
# True


# Not Sorted
numbers = [10, 20, 15, 40, 50]

print(is_sorted_ascending(numbers))

# Output:
# False


# Descending Order
def is_sorted_descending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            return False

    return True


numbers = [50, 40, 30, 20, 10]

print(is_sorted_descending(numbers))

# Output:
# True


# Descending Order - Not Sorted
numbers = [50, 40, 35, 45, 10]

print(is_sorted_descending(numbers))

# Output:
# False


# Edge Cases
print(is_sorted_ascending([]))
# True

print(is_sorted_ascending([5]))
# True

# ============================================================
# Day 9 — Find the Second Largest Distinct Element
# ============================================================

def find_second_largest(numbers):
    largest = None
    second_largest = None

    for number in numbers:

        if largest is None or number > largest:
            second_largest = largest
            largest = number

        elif number != largest and (
            second_largest is None or number > second_largest
        ):
            second_largest = number

    return second_largest


# Example
numbers = [5, 10, 8, 15, 20]

print(find_second_largest(numbers))

# Output:
# 15


# Duplicate Largest Value
numbers = [10, 20, 20, 5]

print(find_second_largest(numbers))

# Output:
# 10


# All Values Equal
numbers = [20, 20, 20]

print(find_second_largest(numbers))

# Output:
# None


# One Element
numbers = [5]

print(find_second_largest(numbers))

# Output:
# None


# Empty Array
numbers = []

print(find_second_largest(numbers))

# Output:
# None


# Negative Values
numbers = [-10, -5, -20, -3]

print(find_second_largest(numbers))

# Output:
# -5