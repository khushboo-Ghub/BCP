# Pattern 14: Numbers increment across rows in triangle pattern
num = 1
for i in range(1, 5):             # Rows from 1 to 4
    line = ''
    for j in range(i):            # Columns for each row
        line += f'{num} '         # Current number
        num += 1                  # Increment
    print(line.strip())           # Print row
