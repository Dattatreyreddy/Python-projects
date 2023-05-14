def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# get input from user
num = int(input("Enter a number: "))

# calculate factorial
fact = factorial(num)

# print result
print("Factorial of", num, "is", fact)
