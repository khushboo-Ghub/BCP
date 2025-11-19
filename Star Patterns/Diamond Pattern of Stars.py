# Pattern 15: Diamond of stars, growing then shrinking
for i in range(1, 6):             # Top half: lines 1 to 5
    print('*' * i)                # Stars increase
for i in range(4, 0, -1):         # Bottom half: lines 4 to 1
    print('*' * i)                # Stars decrease
