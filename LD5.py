# Program to check if number is divisible by 7 OR last digit is 5
a = int(input("Enter a number: "))

if a % 7 == 0 or a % 10 == 5:
    print("Condition satisfied!")
else:
    print("Condition not satisfied")