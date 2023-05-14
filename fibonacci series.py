# get input from user
n = int(input("Enter the number of terms: "))

# initialize variables
a, b = 0, 1

# generate Fibonacci sequence
for i in range(n):
    print(a)
    a, b = b, a + b
