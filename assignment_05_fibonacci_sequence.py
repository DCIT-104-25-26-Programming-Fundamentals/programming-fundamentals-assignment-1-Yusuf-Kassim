# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

import math

def print_fibonacci(n):
    """Part A: Generates and prints the first N terms."""
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    if n == 1:
        print("Fibonacci sequence: 0")
        return

    a, b = 0, 1
    sequence = ["0", "1"]
    
    for _ in range(2, n):
        a, b = b, a + b
        sequence.append(str(b))
        
    print("Fibonacci sequence:", " ".join(sequence))

def check_fibonacci(num):
    """Part B: Checks if a number is in the sequence using a loop."""
    if num < 0:
        print(f"{num} is NOT a Fibonacci number.")
        return

    a, b = 0, 1
    
    # Loop until we hit or pass the target number
    while a < num:
        a, b = b, a + b
        
    if a == num:
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")

def get_valid_input(prompt, check_positive=False):
    """Bulletproof input handler. Trust no user."""
    while True:
        user_input = input(prompt)
        try:
            val = int(user_input)
            if check_positive and val <= 0:
                print("Error: N must be a positive integer.")
                continue
            return val
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

if __name__ == "__main__":
    # PART A
    print("--- PART A: PRINT N TERMS ---")
    n_terms = get_valid_input("How many terms? ", check_positive=True)
    print_fibonacci(n_terms)
    print("\n")

    # PART B
    print("--- PART B: CHECK NUMBER ---")
    target_num = get_valid_input("Enter a number to check: ")
    check_fibonacci(target_num)
