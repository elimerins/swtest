node=int(input())
graph=[[] for _ in range(node + 1)]
parent=[[] for _ in range(node + 1)]
for i in range(node-1):
    root, child = map(int,input().split())
    graph[root].append(child)
    graph[child].append(root)

def dfs(start):
    stack=[start]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            if not parent[i]:
                parent[i].append(node)
                graph[i].remove(node)
                stack.extend(graph[node])

dfs(1)
for i in dfs(1)[2:]:
    print(i[0])
