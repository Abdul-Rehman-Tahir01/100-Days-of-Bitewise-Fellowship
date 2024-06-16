number = input("Enter a number: ")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(f"The factorial of {number} is {factorial(int(number))}")