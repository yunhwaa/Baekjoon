X, Y = map(str, input().split())
re_X = X[-1::-1]
re_Y = Y[-1::-1]
result = str(int(re_X) + int(re_Y))

print(int(result[-1::-1]))