# Pattern 7: Right-align incrementing stars, underscores left
for i in range(5):                 # Rows from 0 to 4
    print(' ' * i + '_ ' * (4-i) + '* ' * (i+1)) # Spaces, underscores, stars
