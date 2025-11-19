# 5.⁠ ⁠Take an integer A as input. You have to tell whether A is divisible by both 5 and 11 or not.

a = int(input("Enter number"))

if( a % 5 == 0 and a % 11 == 0):
    print("Given number is divisible by both 5 & 11")
elif(a % 5 == 0 or a % 11 == 0):
    print(" The given number is only with either 5 or 11")
else:
    print("Not divisible by 5 and 11")

