# You are given 3 integers angles of a triangle. tell wheather the triangle is valid or not ?

# Take input of three angles 
a = int(input("Enter 1st angle: "))
b = int(input("Enter 2nd angle: "))
c = int(input("Enter 3rd angle: "))

# Check validity by using if-else condition
if 1 > 0 and 2 > 0 and 3 > 0 and (1 + 2 + 3 == 180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")