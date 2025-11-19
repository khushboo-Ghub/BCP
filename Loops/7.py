# 7. Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A].
# Input:- A= 4

# Take Input
A = int(input("Enter an integer A: "))
sum = 0
# Apply loops
for i in range(1, A+1, 2):
    sum += i
print(sum)