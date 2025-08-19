# 8
N = int(input("Enter an integer N: "))
count = 0
temp = N
while temp != 0:
    temp = temp // 10
    count += 1
print(count)