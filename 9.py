# 9
N = int(input("Enter an integer N: "))
sum_digits = 0
temp = N
while temp != 0:
    digit = temp % 10
    sum_digits += digit
    temp = temp // 10
print(sum_digits)
