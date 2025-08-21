#find the sum of all the even numbers between 1 and A
A = int(input("Enter an integer A: "))
sum = 0
for i in range(2, A+1, 2):
    sum += i
print(sum)
