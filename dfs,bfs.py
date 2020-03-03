import copy
def bfs(graph,start):
    q =[start]
    visit =[]
    while q:
        node = q[0]
        q.remove(q[0])
        if node not in visit:
            visit.append(node)
            q.extend(graph[node])
    print('BFS :',visit)
def dfs(graph,start):
    stack =[start]
    visit =[]
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            arr=copy.deepcopy(graph[node])
            stack.extend(sorted(arr, reverse=True))

    print('DFS :',visit)
graph = {
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F','G','H'],
    'D':['B','I'],
    'E': ['B'],
    'F': ['C', 'J'],
    'G': ['C', 'K'],
    'H': ['C'],
    'I': ['D'],
    'J': ['F'],
    'K': ['G', 'L'],
    'L': ['K', 'M'],
    'M': ['L', 'N'],
    'N': ['M'],
}
dfs(graph,'A')
bfs(graph,'A')