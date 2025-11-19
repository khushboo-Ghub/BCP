# 8. Take an integer N as input and print the count of digits of that number.
# Input:- N = 10101

# Take Input
N = int(input("Enter an integer N: "))
count = 0
temp = N

# Using While loop
while temp != 0:
    temp = temp // 10
    count += 1
print(count)