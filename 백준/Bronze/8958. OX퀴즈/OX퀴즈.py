T = int(input())
grade = 0
hap = 0

for i in range(1, T+1):
  test = list(input())
  for p in range(0, len(test)):
    if test[p] == "O":
      hap += 1
      grade = grade + hap
    else:
      hap = 0
  print(grade)
  grade = 0
  hap = 0