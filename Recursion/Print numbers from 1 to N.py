# print numbers from 1 to n
def print1toN(n):
    if n == 0:
        return
    print1toN(n - 1)   # first print small numbers
    print(n, end=" ")  # then print current

n = int(input())
print1toN(n)