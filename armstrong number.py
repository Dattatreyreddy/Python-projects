# get input from user
num = int(input("Enter a number: "))

# initialize variables
sum = 0
order = len(str(num))

# check if number is an Armstrong number
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
