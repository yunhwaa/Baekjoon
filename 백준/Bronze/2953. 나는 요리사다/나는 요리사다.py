grade = [int(N) for N in input().split()]
max = sum(grade)
num = 1

for i in range(2, 6):
  grade = [int(N) for N in input().split()]
  if sum(grade) > max:
    max = sum(grade)
    num = i

print("{} {}".format(num, max))