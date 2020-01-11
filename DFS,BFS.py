from queue import Queue
def bfs(graph, start_node):
    visit=set()
    q=Queue()
    q.put(start_node)
    while q.qsize()>0:
        node=q.get()
        if node not in visit:
            visit.add(node)
            for NextNode in graph[node]:
                q.put(NextNode)
    return visit

def dfs(graph, start_node):
    visit = list()
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            graph[node].reverse()
            stack.extend(graph[node])

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