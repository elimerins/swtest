from sys import stdin
input = stdin.readline#input 속도향상
MIS = lambda: map(int,input().split())# lamda식으로 MIS()로 쉽게 사용할 수 있음

from itertools import combinations
n, m = MIS()#숫자 받음
chicken = []
house = []
for i in range(n):
    for j, x in enumerate(MIS()):
        if x == 1: house.append((i,j))
        if x == 2: chicken.append((i,j))
res = float('inf')
for C in combinations(chicken, m):#chicken C m 계산
    #combinations를 사용한 반환값이 chicken의 모든 구성요소 중 m개씩 들어있는 list반환(list length는 그때그때 다름)
    dist = 0#각 C마다 사용될 dist 초기화
    for hx, hy in house:#house 안에들어있는 좌표값 들
        dist+= min((abs(cx-hx)+abs(cy-hy)) for cx, cy in C)
        #각 house마다 C의 각 요소와 min distance를 계속 적립
        #+=를 활용하여 모든 house와 C의 모든 chicken shop의 dist 계산
    res = min(res, dist)
    #C별로 dist값이 다를 수 있으므로 min 계산
print(res)