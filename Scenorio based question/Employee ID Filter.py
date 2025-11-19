n = int(input())
ids = list(map(int, input().split()))
even_id = []

for i in ids:
    if i % 2 == 0:
        even_id.append(i)

if even_id:
    print(*even_id)
else:
    print(-1)