n = int(input())
deadlines = []

for i in range(n):
    x = int(input())
    deadlines.append(x)

k = int(input())

count = 0
for i in range(n):
    for j in range(i, n):
        if deadlines[i] + deadlines[j] == k:
            count = count + 1

print(count)