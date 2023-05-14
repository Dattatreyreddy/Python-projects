# get input from user
n = int(input("Enter the upper limit: "))

# initialize empty list to store prime numbers
primes = []

# check each number from 2 to n for primality
for num in range(2, n+1):
    if all(num % i != 0 for i in range(2, int(num/2)+1)):
        primes.append(num)

# print the list of prime numbers
print("Prime numbers between 2 and", n, "are:", primes)
