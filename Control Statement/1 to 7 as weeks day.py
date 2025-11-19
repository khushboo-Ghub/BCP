# 10.⁠ ⁠WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc.

# First we take an input
d = int(input("Enter the number form 1 to 7: "))

# we apply condition states like (if-else) and printing results 1 by 1
if d == 1:
    print("Sunday hai aaj to bete")
elif d == 2:
    print("Its Monday")
elif d == 3:
    print("Its Tuesday")
elif d == 4:
    print("Its Wednesday")
elif d == 5:
    print("Its Thursday")
elif d == 6:
    print("Its Friday")
elif d == 7:
    print("Its Saturday")
else:
    print("Out of my knowledge")