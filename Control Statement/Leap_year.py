# 9. WAP to check whether a year is a leap year or not.

Year = int(input("Enter year"))

if (Year % 4 == 0 ) and (Year % 400):
    print(f"{Year} This is leap year. ")
else:
    print("This is not leap year")