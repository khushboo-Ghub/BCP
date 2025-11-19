n = int(input())
a = list(map(int, input().split()))

maximum = 0
current = 0

for x in a:
    if x == 0:
        current = current + 1
        if current > maximum:
            maximum = current
    else:
        current = 0

print(maximum)