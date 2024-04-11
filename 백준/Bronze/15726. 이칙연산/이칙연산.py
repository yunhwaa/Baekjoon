A, B, C = map(int, input().split())

num1 = A * B / C
num2 = A / B * C

print(int(max(num1, num2)))