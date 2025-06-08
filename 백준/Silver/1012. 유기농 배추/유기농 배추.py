# 유기농 배추
# 전체 탐색
# dfs -> 큐 이용
import sys
sys.setrecursionlimit(10000) 

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    maze = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    for i in range(k):
        a1, a2 = map(int, input().split())
        maze[a2][a1] = 1

    def dfs(y, x):
        visited[y][x] = 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
        
            if 0 <= ay < n and 0 <= ax < m:
                if maze[ay][ax] == 1 and visited[ay][ax] == 0:
                    dfs(ay, ax)
    
    count = 0
    for y in range(n):
        for x in range(m):
            if maze[y][x] == 1 and visited[y][x] == 0:
                dfs(y, x)
                count += 1

    print(count)