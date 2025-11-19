# 9. Take an integer N as input. Your task is to calculate and print the sum of the digits of the given number N.
# Input:- N = 1589


# Take Input
N = int(input("Enter an integer N: "))
sum_digits = 0
temp = N

# using while loop for this condition
while temp != 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10
print(sum_digits)
