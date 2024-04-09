K, N, M = map(int, input().split())

left_money = K * N - M
if left_money < 0:
  print(0)
else:
  print(left_money)