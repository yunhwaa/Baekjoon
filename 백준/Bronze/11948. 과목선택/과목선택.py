A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())

test1 = A + B + C + D - min(A, B, C, D)
test2 = max(E, F)

print(test1 + test2)