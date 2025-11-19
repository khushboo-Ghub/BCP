n = int(input())
sales = list(map(int, input().split()))

max_sale = max(sales)
min_sale = min(sales)

print(max_sale, min_sale)