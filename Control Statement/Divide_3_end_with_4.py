# take input
a = int(input("Enter a number: "))

# Check its divided or not
if (a % 3 == 0 or a % 10 == 4):
    print("The number is divisible by 3 and its last digit is 4.")
else:
    print("Condition not satisfied.")