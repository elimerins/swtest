from collections import deque

# 섬에 넘버링
def numbering_irlands(x, y):
    arr[y][x] = irland
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[y][x] = 1

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if not visited[ny][nx] and arr[ny][nx]:
                arr[ny][nx] = irland
                q.append((nx, ny))
                visited[ny][nx] = 1


def get_min_distance(irland):
    global min_

    distance = [[-1]*N for _ in range(N)]
    q = deque()
    for y in range(N):
        for x in range(N):
            if arr[y][x] == irland:
                q.append((x, y))
                distance[y][x] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[ny][nx] != irland and arr[ny][nx]:
                min_ = min(min_, distance[y][x])
                return
            if distance[ny][nx] == -1 and not arr[ny][nx]:
                distance[ny][nx] = distance[y][x] + 1
                q.append((nx, ny))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
min_, irland = 1e9, 1

for y in range(N):
    for x in range(N):
        if not visited[y][x] and arr[y][x]:
            numbering_irlands(x, y)
            irland += 1

for i in range(1, irland):
    get_min_distance(i)

print(min_)
