N = int(input())
arr=[[0]*10 for _ in range(10)]
arr[0] = [1,1,1,1,1,1,1,1,1,1]
i = 1
while i < N:
    for j in range(1,10):
        for k in range(9,j,-1):
            arr[i][j]=arr[i-1][k]
    i+=1
print(sum(arr)%1000000000)