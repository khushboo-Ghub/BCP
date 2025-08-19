# 7. Read three angles of triangles and determine their types(Right triangle, Obtuse triangle, Acute triangle).
# take input from user of angle 1 ,2 and 3
ang1 = int(input("enter angle1: "))
ang2 = int(input("enter angle2: "))
ang3 = int(input("enter angle3: "))

# check which triangle is it based on inputs
if(ang1 > 90 or ang2 > 90 or ang3 > 90):
    print("this triangle is obtuse triangle")
elif(ang1 == 90 or ang2 == 90 or ang3 == 90):
    print("triangle is obtuse triangle")
else:
    print("actute angle")


