T = int(input())
for p in range(1, T+1):
  N = input()
  re_N = N[-1:-len(N)-1:-1]
  sum_N = int(N) + int(re_N)

  sum_N = str(sum_N)

  if sum_N[0:len(sum_N)//2] == sum_N[-1:-(len(sum_N)//2)-1:-1]:
    print("YES")
  else:
    print("NO")