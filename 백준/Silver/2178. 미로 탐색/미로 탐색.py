from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().strip()))) 

visited = [[0] * m for _ in range(n)]

def bfs(graph, visited, start_x, start_y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # queue = deque([start])
    queue = deque()
    queue.append((start_x, start_y))
    # visited[start] = True
    visited[start_y][start_x] = 1

    while queue:
        x, y = queue.popleft()
        # for i in graph[v]:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if not visited[i]:
            #     queue.append(i)
            #     visited[i] = True
            if 0 <= nx < m and 0 <= ny < n:
                if maze[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((nx, ny))

bfs(maze, visited, 0, 0)
print(visited[n-1][m-1])