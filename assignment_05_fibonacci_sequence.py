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

def generate_fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    if n <= 0:
        return None
    sequence = [0, 1]
    if n == 1:
        return [0]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def is_fibonacci_number(value):
    """Return True if value is a Fibonacci number, False otherwise."""
    if value < 0:
        return False
    a, b = 0, 1
    while a < value:
        a, b = b, a + b
    return a == value


def main():
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if n <= 0:
        print("Error: Please enter a valid positive integer.")
        return

    fibonacci_sequence = generate_fibonacci(n)
    print("Fibonacci sequence:", " ".join(str(num) for num in fibonacci_sequence))

    try:
        number_to_check = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if is_fibonacci_number(number_to_check):
        print(f"{number_to_check} is a Fibonacci number.")
    else:
        print(f"{number_to_check} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

