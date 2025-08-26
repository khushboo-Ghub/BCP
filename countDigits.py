# print the count of digits of N number
n = int(input("Enter a number "))
count = 0
d = n
while d!= 0:
    d = d // 10
    count += 1
print(count)
