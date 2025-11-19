# Write a program to input three number and print the minimum among them ?

# Take input of 3 number by user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
# We use if-else condition for "Minimum number"
minimum = a
if b < minimum:
    minimum = b
if c < minimum:
    minimum = c
# printing the value
print("The minimum number is:", minimum)
