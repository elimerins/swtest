from collections import deque
n, m = map(int,input().split(" "))

arr = [[int(x) for x in input()] for _ in range(n)]
visited = [[0]*m for _ in range(n)]
irland = 0

dx = [0, 0,1,-1]
dy = [1,-1,0, 0]

def bfs(x,y):
    global irland
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        arr[x][y]=irland
        for i in range(4):
            nx, ny = x + dx[i],y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and arr[nx][ny] == 1:
                    visited[nx][ny] = 1
                    arr[nx][ny] = irland
                    q.append((nx,ny))

def bfs2(irland):
    global ans
    dist =[[-1]*m for _ in range(n)]
    q = deque()
    for x in range(n):
        for y in range(m):
            if arr[x][y] == irland:
                dist[x][y] = 0
                q.append((x, y))
                #섬에 해당하는 부분 0으로 처리하여 거리 계산하기 위함

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i],y + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if arr[nx][ny] != irland and arr[nx][ny]:
                # 도달한 arr.nx.ny 값이 다른 섬이어야함. 0도 아니어야함
                    ans = min(ans,dist[x][y])
                    #현 dist.nx.ny 값과 ans값을 비교하여 ans 도출함
                    continue
                if dist[nx][ny] == -1:
                    #방문하지 않은 곳이라면,
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))


for x in range(n):
    for y in range(m):
        if not visited[x][y] and arr[x][y]:
            irland += 1
            visited[x][y]=1
            bfs(x, y)

ans = 1e9
for i in range(1,irland):
    bfs2(i)
print(ans)