# you are given 3 integer angles of a triangle.Tell whether the triangle is valid or not

a = int(input("Enter 1st angle: "))
b = int(input("Enter 2nd angle: "))
c = int(input("Enter 3rd angle: "))

# Check validity by using if-else condition
if (a+b+c == 180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")