min = [int(x) for x in input().split()]
man = [int(y) for y in input().split()]

if sum(min) >= sum(man):
  print(sum(min))
else:
  print(sum(man))