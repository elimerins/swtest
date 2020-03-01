def bfs():
    bfs(graph,'A')
def bfs(graph, start_node):
    visit=[]
    queue=[start_node]

    while queue:
        node=queue.pop(0)
        if node not in visit:
            visit.append(node)
            #arr=graph[node]
            #arr.reverse()
            queue.extend(graph[node])
    return visit
def dfs():
    dfs(graph,'A')
def dfs(graph, start_node):
    visit = list()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            arr=graph[node]
            arr.reverse()
            stack.extend(arr)

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