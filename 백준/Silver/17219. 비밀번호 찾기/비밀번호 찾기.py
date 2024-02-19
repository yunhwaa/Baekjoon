N, M = map(int, input().split())
note = {}

for i in range(0, N):
  address, key = input().split()
  note[address] = key

for j in range(0, M):
  find_address = input()
  print(note[find_address])