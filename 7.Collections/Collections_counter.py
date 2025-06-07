from collections import Counter

# Number of shoes
shoes = int(input())
shoes_list = list(map(int, input().split()))
inventory = Counter(shoes_list)

cust = int(input())

earnings = 0

for _ in range(cust):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1  # Reduce the stock after sale

print(earnings)
