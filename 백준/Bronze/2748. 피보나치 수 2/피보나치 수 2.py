n = int(input())

df = [0] * 91
df[0], df[1], df[2] = 0, 1, 1

for i in range(3, n+1):
  df[i] = df[i-1] + df[i-2]

print(df[n]) 