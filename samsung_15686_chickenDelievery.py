N,M = map(int,input().split())

maps = [[int(x) for x in input().split()] for _ in range(N)]

house = []
shop = []
pick = []
ret = 100000
def dfs(pos):
    if (len(pick) == M):
        candi = 0
        for i in range(len(house)):
            min_dist=100000
            for j in range(len(pick)):
                min_dist = min(min_dist,abs(house[i][0] - pick[j][0])+abs(house[i][1] - pick[j][1]))
            candi += min_dist

        global ret
        if (ret > candi):
            ret = candi

        return

    for i in range(pos,len(shop)):
        pick.append(shop[i])
        dfs(i + 1)
        pick.pop()

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            house.append([i, j])
        if maps[i][j] == 2:
            shop.append([i, j])

dfs(0)
print(ret)




