# print all subarrays
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i, n):
        # printing subarray from i to j
        for k in range(i, j + 1):
            print(arr[k], end=" ")
        print()