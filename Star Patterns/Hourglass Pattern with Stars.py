# Pattern 9: Hourglass of stars with spaces in middle
n = 5                               # Set n as half of lines
for i in range(n, 0, -1):           # Loop from n down to 1
    print('*' * i + ' ' * (2*n - 2*i) + '*' * i) # Left stars, spaces, right stars
