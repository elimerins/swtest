import sys
sys.setrecursionlimit(10**8)
def dfs(v,visit):
    global cnt
    if v not in visit:
        visit.append(v)
        dfs(graph[v],visit)
    elif v is visit[-1] and result[v] != True:
        result[v] = True
        cnt += 1
    elif v in visit and v not in result:
        arr = visit[visit.index(v):]
        result.extend(arr)

T = int(input())
graph = {}

cnt = 0
for _ in range(T):
    N = int(input())
    result = [False]*(N+1)
    Mem =list(map(int,sys.stdin.readline().split()))

    for idx,i in enumerate(Mem):
        graph[idx+1]=i
    for i in graph:
        visit = list()
        dfs(graph[i],visit)
print(N-len(result))