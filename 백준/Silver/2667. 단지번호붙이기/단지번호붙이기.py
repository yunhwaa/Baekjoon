n = int(input())
maze = []
for i in range(n):
    maze.append(list(map(int, input().strip())))

visited = [[0]*n for _ in range(n)]
answer = []

def dfs(x, y):
    visited[x][y] = 1
    count = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    #for i in maze[x][y]:
    for i in range(4):
        ax = x + dx[i]
        ay = y + dy[i] 
        if 0 <= ax < n and 0 <= ay < n:
            if maze[ax][ay] == 1 and visited[ax][ay] == 0:
                count += dfs(ax, ay)
    return count 

for i in range(n):
    for j in range(n):
        if maze[i][j] == 1 and visited[i][j] == 0:
            area_size = dfs(i, j)
            answer.append(area_size)

answer = sorted(answer)

print(len(answer))
for i in answer:
    print(i)