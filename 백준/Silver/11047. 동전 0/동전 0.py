# 동전 0
n, k = map(int, input().split())
coin = []
sum = 0
count = 0

for i in range(n):
    coin.append(int(input()))

coin = sorted(coin, reverse = True)

for c in coin:
    if k >= c:
        count += k // c
        k = k % c

print(count)