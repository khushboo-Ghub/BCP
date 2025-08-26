#check whether a number is palindrome or not
a = int(input("Enter a number "))
real = a
rev = 0
while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10
if real == rev:
    print("Yes, it's a palindrome number")
else:
    print("No, it's not a palindrome number")
