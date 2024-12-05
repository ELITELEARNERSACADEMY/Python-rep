#Python Program to Find Fibonacci Numbers using Recursion
#0 1 1 2 3 5 
def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
                  




# Test the function
num_terms = int(input("Enter the position of the Fibonacci number you want: "))
result = fibonacci(num_terms)
print(f"The {num_terms}th Fibonacci number is: {result}")

