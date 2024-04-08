N = int(input())
S = [str(N) for N in input()]
count = 0

for i in range(0, len(S)):
  if S[i] == "j":
    count += 2
  elif S[i] == "o":
    count += 1
  elif S[i] == "i":
    count += 2

print(count)