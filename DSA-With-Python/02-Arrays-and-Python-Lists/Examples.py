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

numbers = [4, 7, 2, 9, 5]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Maximum:", maximum)


# Array Traversal — Find Minimum

numbers = [10, 5, 2, 8, 3]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Minimum:", minimum)


# Array Traversal — Calculate Sum

numbers = [10, 20, 30, 40]

sum_numbers = 0

for number in numbers:
    sum_numbers = sum_numbers + number

print("Sum:", sum_numbers)


# Array Traversal — Count Occurrences

numbers = [10, 20, 30, 30, 40, 30]

target = 30

repeat_number = 0

for number in numbers:
    if number == target:
        repeat_number += 1

print("Occurrences:", repeat_number)


# Find Minimum Using Function

def find_minimum(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


numbers = [10, 5, 2, 8, 3]

print("Function Minimum:", find_minimum(numbers))


# Calculate Sum Using Function

def calculate_sum(numbers):
    sum_numbers = 0

    for number in numbers:
        sum_numbers = sum_numbers + number

    return sum_numbers


numbers = [10, 20, 30, 40]

print("Function Sum:", calculate_sum(numbers))


# Count Occurrences Using Function

def count_occurrences(numbers, target):
    repeat_number = 0

    for number in numbers:
        if number == target:
            repeat_number += 1

    return repeat_number


numbers = [10, 20, 30, 30, 40, 30]

print("Function Occurrences:", count_occurrences(numbers, 30))