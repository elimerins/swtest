def dsf(v):
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dsf(e)

N,M = map(int,input().split())
adj = [[] for i in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for i in range(M):
    input_data=list(map(int,input().split()))
    adj[input_data[0]].append(input_data[1])
    adj[input_data[1]].append(input_data[0])

for i in range(1,len(visited)):
    if not(visited[i]):
        cnt +=1
        dsf(i)
print(cnt)