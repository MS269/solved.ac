from collections import deque


MAX = 10 ** 5 + 1

n, k = map(int, input().split())
visited = [[-1, 0] for _ in range(MAX)]


def bfs(x):
    q = deque([x])
    visited[x] = [0, 1]

    while q:
        x = q.popleft()

        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < MAX:
                if visited[nx][0] == -1:
                    q.append(nx)
                    visited[nx] = [visited[x][0] + 1, visited[x][1]]
                elif visited[nx][0] == visited[x][0] + 1:
                    visited[nx][1] += visited[x][1]

    return visited[k]


print(*bfs(n), sep="\n")
