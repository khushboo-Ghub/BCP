# 6. You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A. Even numbers are those numbers that are divisible by 2.
# Input:- A = 5

# Take Input
A = int(input("Enter an integer A: "))
sum = 0
# Loop for checking
for i in range(2, A+1, 2):
    sum += i
print(sum)
