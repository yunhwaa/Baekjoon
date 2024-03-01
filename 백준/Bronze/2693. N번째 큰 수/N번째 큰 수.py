T = int(input())
N = 10
for i in range(1, T+1):
  num = [int(N) for N in input().split()]
  num.sort(reverse=True)
  print(num[2])