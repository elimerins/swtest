import sys
read = lambda : sys.stdin.readline.strip()

n = int(read())

def dfs(matrix,cnt,x,y):

    matrix[x][y] = 0
    n_x = [1, -1, 0, 0]
    n_y = [0, 0, 1, -1]
    for i in range(4):
        d_x = x + n_x[i]
        d_y = y + n_y[i]

        if d_x < n and d_x >= 0 and d_y <n and d_y >= 0:
            if matrix[d_x][d_y] == 1:
                cnt = dfs(matrix,cnt+1,d_x,d_y)

    return cnt

matrix = [list(map(int,list(read()))) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            ans.append(dfs(matrix,1,i,j))

print(len(ans))
for _ in sorted(ans):
    print(_)
