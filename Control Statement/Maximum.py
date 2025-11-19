# 6.⁠ ⁠Read three integers and print their maximum.

a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd no. : "))


if(c < a and b < a):
    print(f"{a} is maximum number ")
elif(a < b and c < b):
    print(f" {b} is maximum number ")
else:
    print(f"{c} is maximum number")

