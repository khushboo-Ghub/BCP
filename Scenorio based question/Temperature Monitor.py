n = int(input())
temp = list(map(int, input().split()))

total = 0
for t in temp:
    total = total + t

avg = total / n

count = 0
for t in temp:
    if t > avg:
        count = count + 1

print(count)