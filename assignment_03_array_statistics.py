# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def calc_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calc_average(numbers):
    total = calc_sum(numbers)
    return total / len(numbers)


def calc_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def calc_min(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


# Main block
n = int(input("How many numbers? "))

if n <= 0:
    print("Error: N must be a positive integer.")
else:
    numbers = []
    for i in range(1, n + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)
    
    print("\nResults:")
    print(f"Sum:     {calc_sum(numbers)}")
    print(f"Average: {calc_average(numbers)}")
    print(f"Maximum: {calc_max(numbers)}")
    print(f"Minimum: {calc_min(numbers)}")
