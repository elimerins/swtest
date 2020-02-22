import copy
def bfs(graph, start_node):
    visit=[]
    q=[start_node]
    while q:
        node=q[0]
        q.remove(q[0])
        if node not in visit:
            visit.append(node)
            q.extend(graph[node])

    return visit

def dfs(graph, start_node):
    visit = list()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            #arr=copy.deepcopy(graph[node])
            #arr.reverse()
            stack.extend(sorted(graph[node],reverse=True))

    return visit

if __name__ == "__main__":
    graph = {
        'A':['B'],
        'B': ['A','C','H'],
        'C': ['B','D'],
        'D': ['C','E','G'],
        'E': ['D','F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B','I','J','M'],
        'I': ['H'],
        'J': ['H','K'],
        'K': ['J','L'],
        'L': ['K'],
        'M': ['H']
    }
    print("BFS :",bfs(graph,'A'))
    print("DFS :",dfs(graph,'A'))