# Pattern 11: Hourglass then reversed hourglass
n = 5
for i in range(n, 0, -1):           # First hourglass
    print('*' * i + ' ' * (2*n - 2*i) + '*' * i)
for i in range(1, n+1):             # Then reversed hourglass
    print('*' * i + ' ' * (2*n - 2*i) + '*' * i)
