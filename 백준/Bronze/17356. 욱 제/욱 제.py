A, B = map(int, input().split())
M = (B-A) / 400

num = 1 / (1+10**M)
print(num)