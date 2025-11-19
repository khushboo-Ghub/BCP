# Pattern 6: Top-down decrease of underscores between border stars
for i in range(5, 0, -1):      # Loop from 5 down to 1
    print('*' + '_ ' * (i-1) + '*') # First star, (i-1) underscores, last star
