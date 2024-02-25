A, B = map(str, input().split())

re_A = int(A[-1::-1])
re_B = int(B[-1::-1])

if re_A >= re_B:
  print(re_A)
else:
  print(re_B)