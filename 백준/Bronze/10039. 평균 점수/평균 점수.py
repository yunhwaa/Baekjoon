grade = []
for i in range(1, 6):
  num = int(input())
  if num < 40:
    num = 40
  grade.append(num)

print(round(sum(grade) / 5))