# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input from user.
# Input:- N = 10

# Take Input
N = int(input("Enter a positive integer N: "))
# Apply loop
for i in range(1, N+1, 2):
    print(i, end=' ')