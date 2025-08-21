#find the sum of all natural numbers from 1 to N
N = int(input("Enter a positive integer N: "))
sum = 0
for i in range(1, N+1):
    sum += i
print(sum)
