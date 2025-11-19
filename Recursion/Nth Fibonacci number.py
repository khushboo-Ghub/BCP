# fibonacci using recursion
def fib(n):
    if n <= 1:         # 0 or 1 return itself
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))