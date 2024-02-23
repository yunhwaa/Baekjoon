N = int(input())
hap = 0
grade = [int(N) for N in input().split()]

M = max(grade)
for i in range(0, len(grade)):
  hap += grade[i] / M * 100

print(hap/N)