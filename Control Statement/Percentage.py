# acccept the percentages from the user and display the grade according to criteria ?

# Accept percentage from the user
percentage = float(input("Enter your percentage: "))

# Determine the grade based on the percentage
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

# Display the result
print(f"Your grade is: {grade}")