def dsf(v):
    visited[v] = True
    for e in graph[v]:
        if not(visited[e]):
            dsf(e)

T = int(input())

cnt = 0
for _ in range(T):
    M = int(input())
    visited = [False] * (M + 1)
    graph = {}
    path=list(map(int,input().split()))
    for idx,i in enumerate(path):
        graph[idx+1]=[i]
    for i in range(1,len(visited)):
        if not(visited[i]):
            cnt +=1
            dsf(i)
    print(cnt)