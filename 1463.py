from collections import deque


n = int(input())


def bfs(x):
    q = deque([x])
    visited = [-1] * (x + 1)
    visited[x] = 0

    while q:
        x = q.popleft()

        if x == 1:
            return visited[x]

        if x % 3 == 0 and visited[x // 3] == -1:
            q.append(x // 3)
            visited[x // 3] = visited[x] + 1
        if x % 2 == 0 and visited[x // 2] == -1:
            q.append(x // 2)
            visited[x // 2] = visited[x] + 1
        if visited[x - 1] == -1:
            q.append(x - 1)
            visited[x - 1] = visited[x] + 1


print(bfs(n))
