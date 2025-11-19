# sum from L to R (1-based index)
n = int(input())
arr = list(map(int, input().split()))
L, R = map(int, input().split())

s = 0
for i in range(L - 1, R):
    s += arr[i]

print(s)