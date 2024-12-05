def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b  # Update values for the next Fibonacci number
    return b

# Test the function
num_terms = int(input("Enter the position of the Fibonacci number you want: "))
result = fibonacci(num_terms)
print(f"The {num_terms}th Fibonacci number is: {result}")

