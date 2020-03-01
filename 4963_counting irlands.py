import sys
read = lambda : sys.stdin.readline()

while 1:
    w,h = map(int,input().split())
    matrix = [list(map(int,list(read().strip()))) for _ in range(w)]
    ans = []

    def dfs(x,y):

        matrix[x][y] = 0
        n_x = [1, 1, 1,-1,-1,-1, 0, 0]
        n_y = [0, 1,-1, 0, 1,-1, 1,-1]
        for i in range(8):
            d_x = x + n_x[i]
            d_y = y + n_y[i]

            if 0<=d_x < h and 0<=d_y <w:
                if matrix[d_x][d_y] == 1:
                    dfs(d_x,d_y)
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                cnt += 1
                dfs(i,j)

    print(cnt)

