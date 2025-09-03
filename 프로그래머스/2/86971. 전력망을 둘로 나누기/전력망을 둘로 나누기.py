from collections import deque

def solution(n, wires):
    def bfs(start, graph):
        visited = [False] * (n+1)
        queue = deque([start])
        visited[start] = True
        count = 1
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count
    
    min_diff = n
    for i in range(len(wires)):
        graph = [[] for _ in range(n+1)]
        for j, (a, b) in enumerate(wires):
            if i != j:
                graph[a].append(b)
                graph[b].append(a)
        count = bfs(1, graph)
        diff = abs(count - (n-count))
        min_diff = min(min_diff, diff)
    return min_diff