N = int(input())
S = input()
count = 0

for i in range(0, N):
  if S[i] == 'a' or S[i] == 'e' or S[i] == 'i' or S[i] == 'o' or S[i] == 'u':
    count += 1
print(count)