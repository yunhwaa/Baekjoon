N = int(input())

for i in range(1, N+1):
  number = input()
  if len(number) >= 6 and len(number) <= 9:
    print("yes")
  else:
    print("no")