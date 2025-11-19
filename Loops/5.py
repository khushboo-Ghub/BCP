# 5. Write a program to find the sum of all Natural numbers from 1 to N, where you have to take N as input from user
# Input:- N = 10

# Take Input
N = int(input("Enter a positive integer N: "))

# Using For loop
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)