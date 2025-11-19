# Pattern 12: Numbers increase each row from 1
for i in range(1, 5):             # Rows from 1 to 4
    print(' '.join(str(j) for j in range(1, i+1))) # From 1 to i
