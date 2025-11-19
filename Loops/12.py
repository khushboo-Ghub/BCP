# 12. You are given two integers A and B. You have to find the value of A^B.
# Input:- A = 2 , B = 3


# Take 1st Input
A = int(input("Enter integer A 🫵"))

# Take 2nd Input
B = int(input("Enter integer B 🫵 "))

# Declare results as 1
result = 1

# Using for loop
for _ in range(B):
    result *= A
print(result)
