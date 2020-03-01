import sys
sys.setrecursionlimit(10**8)

read=sys.stdin.readline

def dfs(x, path):
    global CNT, visited, g
    path.append(x)
    visited[x]=1
    if visited[g[x]]:
        if x==g[x]:#1:1 check
            CNT+=1
        else:#cycle check
            try:
                CNT+=len(path)-path.index(g[x])
            except:
                return
    else:
        dfs(g[x], path)

t=int(read())

while t:
    t-=1
    CNT=0
    n=int(read())
    visited=[0]*(n+1)
    g=[0]+list(map(int, read().split()))
    for i in range(1, n+1):
        if not visited[g[i]]:
            dfs(g[i], [])
    print(n-CNT)
