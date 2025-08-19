# WAP to input three numbers and print the minimum among them

#  accept the percentage from the user and display the grade according to criteria.


a = int(input("number 1: "))
b = int(input("number 2: "))
c = int(input("number 3: "))

if(c>a<b):
    print(f"{a} is the minimum number")
elif(a>b<c):
    print(f"{b} is the minimum number")
else:
    print(f"{c} is the minimum number")
