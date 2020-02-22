from collections import deque

n,m=map(int,input().split(" "))
dx = [1,-1,0, 0]
dy = [0, 0,1,-1]
arr=[[int(x) for x in input()] for _ in range(n)]
check=[[False]*m for _ in range(n)]
q=deque()
q.append((0,0))
while q:
    x,y = q.popleft()
    check[x][y] = True
    for i in range(4):
        nx,ny = x + dx[i],y + dy[i]

        if 0 <= nx <n and 0 <= ny <m:
            if arr[nx][ny] == 1 and check[nx][ny] == False:
                check[nx][ny] = True
                arr[nx][ny] = arr[x][y]+1
                q.append((nx,ny))
print(arr[n-1][m-1]-1)

