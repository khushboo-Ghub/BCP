#find the sum of all the odd numbers between 1 and A
A = int(input("Enter an integer A: "))
sum = 0
for i in range(1, A+1, 2):
    sum += i
print(sum)
