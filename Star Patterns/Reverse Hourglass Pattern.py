# Pattern 10: Reversed hourglass of stars
n = 5                               # Use same n
for i in range(1, n+1):             # Loop from 1 up to n
    print('*' * i + ' ' * (2*n - 2*i) + '*' * i) # Left stars, spaces, right stars
