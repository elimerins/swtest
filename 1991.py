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
        visit += node
        if node_graph[node][1] != '.':
            stack.append(node_graph[node][1])
        if node_graph[node][0] != '.':
            stack.append(node_graph[node][0])

    return visit
#inorder
def inorder(node_graph, root):
    stack=[root]
    visit = ''
    while stack:
        if node_graph[stack[-1]][0] != '.' and node_graph[stack[-1]][0] not in visit:
            stack.append(node_graph[stack[-1]][0])
        else:
            node=stack.pop()
            visit += node
            if node_graph[node][1] != '.':
                stack.append(node_graph[node][1])

    return visit
#postorder
def postorder(node_graph, root):
    stack = [root]
    visit = ''
    while stack:
        if node_graph[stack[-1]][0] != '.' and node_graph[stack[-1]][0] not in visit:
            stack.append(node_graph[stack[-1]][0])
        elif node_graph[stack[-1]][1] == '.' or node_graph[stack[-1]][1] in visit:
            visit += stack.pop()#root node append
        else:
            stack.append(node_graph[stack[-1]][1])
    return visit


print(preorder(node_graph,"A"))
print(inorder(node_graph,"A"))
print(postorder(node_graph,'A'))