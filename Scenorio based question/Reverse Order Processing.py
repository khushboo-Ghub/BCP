n = int(input())
ids = list(map(int, input().split()))

ans = []
for i in range(n-1, -1, -1):
    if ids[i] % 5 == 0:
        ans.append(ids[i])

if len(ans) == 0:
    print(-1)
else:
    for x in ans:
        print(x, end=" ")