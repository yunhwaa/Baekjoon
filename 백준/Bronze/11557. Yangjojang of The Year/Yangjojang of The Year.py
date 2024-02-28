T = int(input())

for i in range(1, T+1):
  N = int(input())
  spend = {}
  for j in range(1, N+1):
    S, L = map(str, input().split())
    spend[S] = int(L)
  

  print(max(spend, key=spend.get))