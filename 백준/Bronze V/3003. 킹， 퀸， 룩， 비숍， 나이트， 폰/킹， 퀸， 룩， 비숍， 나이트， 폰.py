piece = [1, 1, 2, 2, 2, 8]

set = list(input().split())
need = []

for i in range(0, len(piece)):
    print(int(piece[i]) - int(set[i]), end=" ")