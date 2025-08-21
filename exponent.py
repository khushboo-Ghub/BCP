#find the value of A^B
A = int(input("Enter integer A: "))
B = int(input("Enter integer B: "))
result = 1
for _ in range(B):
    result *= A
print(result)
