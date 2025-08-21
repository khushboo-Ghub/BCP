#print A's multiplication table having the first 10 multiples
A = int(input("Enter an integer A: "))
for i in range(1, 11):
    print(f"{A} * {i} = {A*i}")
