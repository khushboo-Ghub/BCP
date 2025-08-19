# print the maximum

a = int(input("number 1: "))
b = int(input("number 2: "))
c = int(input("number 3: "))

if(c<a>b):
    print(f"{a} is the maximum number")
elif(a<b>c):
    print(f"{b} is the maximum number")
else:
    print(f"{c} is the maximum number")
