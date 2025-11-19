# 10. You are given an integer A as input, and you need to determine whether it is a palindrome
# or not. A palindrome integer is one whose digits, when reversed, result in the same number.
# For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome
# because its reverse is 321.Note: The given integer will not have any leading zeros.
# Input:- A = 131


# Take Input
A = int(input("Enter an integer A: "))
original = A
reverse = 0

# Check using while loop
while A > 0:
    digit = A % 10
    reverse = reverse * 10 + digit
    A = A // 10

# Using conditional statement
if original == reverse:
    print("Yes")
else:
    print("No")
