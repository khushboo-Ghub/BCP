#print all odd numbers from 1 to N 
N = int(input("Enter a positive integer N: "))
for i in range(1, N+1, 2):
    print(i, end=' ')
