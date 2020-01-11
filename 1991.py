node=int(input())
node_graph={i:[] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for _ in range(node):
    node, left, right = map(str,input().split())
    node_graph[node] += [left,right]
#preorder
def preorder(node_graph, root):
    stack = [root]
    visit = ''
    while stack:
        node = stack.pop()
        if node not in visit and node != '.':
            visit += node
            stack.append(node_graph[node][1])
            stack.append(node_graph[node][0])

    return visit
#inorder
def inorder(node_graph, root):
    stack=[]
    visit = ''
    node=root
    while(True):
        while(node != "."):
            stack.append(node)
            node = node_graph[node][0]
        if stack:
            node = stack.pop()
            visit += node
            node = node_graph[node][1]
        else:
            break
    return visit

print(preorder(node_graph,"A"))
#print(inorder(node_graph,"A"))