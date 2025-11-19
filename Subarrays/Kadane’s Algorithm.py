# kadane algo for max subarray sum
n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
curr = 0

for x in arr:
    curr = curr + x        # add element
    if curr > max_sum:     # update max
        max_sum = curr
    if curr < 0:           # reset if negative
        curr = 0

print(max_sum)