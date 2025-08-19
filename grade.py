# accept the percentage from the user and display the grade according to criteria.

percent = int(input("enter your percentage please: "))

if(percent >= 85):
    print("congrats! A+ grade")
elif(percent >= 65 and percent < 85):
    print("A grade")
elif(percent >= 45 and percent < 65):
    print("B grade")
elif(percent >= 25 and percent < 45):
    print("C grade")
else:
    print("D")