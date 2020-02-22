import copy
def bfs(graph,start_node):
    visit=list()
    q=[start_node]
    while q:
        node=q[0]
        q.remove(q[0])
        if node not in visit:
            visit.append(node)
            print(node,end=' ')
            q.extend(graph[node])
def dfs(graph,start_node):
    visit = list()
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            print(node,end=" ")
            arr = copy.deepcopy(graph[node])
            arr.reverse()
            stack.extend(arr)
    return visit

n, m, v = map(int,input().split(" "))
graph = {}
for i in range(1,n+1):
    graph[i]=[]
for i in range(0,m):
    idx, value = map(int,input().split(" "))
    if idx not in graph[value]:
        graph[value].append(idx)
    if value not in graph[idx]:
        graph[idx].append(value)
for i in range(1,n+1):
    graph[i].sort()
dfs(graph,v)
print()
bfs(graph,v)