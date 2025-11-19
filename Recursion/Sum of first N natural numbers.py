# function to find sum of first N numbers
def sumN(n):
    if n == 0:      # base case
        return 0
    return n + sumN(n - 1)   # adding n again and again

n = int(input())
print(sumN(n))