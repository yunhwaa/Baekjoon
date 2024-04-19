L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

num1 = A // C
num2 = B // D 

if A % C != 0:
  num1 += 1
if B % D != 0:
  num2 += 1

num = max(num1, num2)

print(L - num)
