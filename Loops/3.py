# 3. Write a program to print all even numbers from 1 to N, where you have to take N as input from the user.
# Input:- N = 10

# Take Input
N = int(input("Enter a positive integer N: "))

# Apply For loop
for i in range(2, N+1, 2):
    print(i, end=' ')