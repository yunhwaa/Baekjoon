def solution(m, n, puddles):
    answer = 0
    mod = 1_000_000_007
    maze = [[0]*m for _ in range(n)]
    for p in puddles:
        a, b = p[0], p[1]
        maze[b-1][a-1] = -1
    
    for y in range(n):
        for x in range(m):
            if maze[y][x] == -1:
                maze[y][x] = 0
                continue
                
            if y == 0 and x == 0:
                maze[y][x] = 1
                continue
            
            val = 0
            if y > 0:
                val += maze[y-1][x]
            
            if x > 0:
                val += maze[y][x-1]
            maze[y][x] = val % mod
    return maze[n-1][m-1]