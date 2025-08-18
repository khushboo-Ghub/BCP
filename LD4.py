# check if the number is divisible by 3 and if it's last digit is 4

num = int(input("Enter a number: "))

if (num % 3 == 0 and num % 10 == 4):
    print("The number is divisible by 3 and its last digit is 4.")
else:
    print("Condition not satisfied.")
