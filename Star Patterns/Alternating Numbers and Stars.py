# Pattern 4: Print numbers and stars alternating on each row

# Loop for 5 rows, length increases by 1 each time
for i in range(1, 6):          
    line = ''
    for j in range(1, i+1):    
        if j % 2 != 0:         
            line += f'{j} '
        else:                  
            line += '* '
    print(line.strip())        
