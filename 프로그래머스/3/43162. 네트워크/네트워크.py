def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, i, visited)
            count += 1
    return count

## 1 2 3
#1 1 1 0
#2 1 1 0
#2 0 0 1

def dfs(graph, v, visited):
    visited[v] = True
    for i in range(len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)
            