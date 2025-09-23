n = int(input())
codes = list(map(int, input().split()))

ans = []
for i in codes:
    if codes.count(i) == 1:
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    for x in ans:
        print(x, end=" ")