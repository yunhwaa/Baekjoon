x, y, w, h = map(int, input().split())
a = x - 0
b = y - 0
c = w - x
d = h - y

print(min(a, b, c, d))