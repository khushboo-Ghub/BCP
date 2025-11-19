# count digits using recursion
def count(n):
    if n == 0:
        return 0
    return 1 + count(n // 10)

n = int(input())
print(count(n))