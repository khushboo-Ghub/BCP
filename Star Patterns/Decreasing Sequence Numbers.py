# Pattern 13: Numbers decrease each row from 4
for i in range(4, 0, -1):         # Rows from 4 to 1
    print(' '.join(str(j) for j in range(1, i+1))) # From 1 to i
