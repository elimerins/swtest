N = int(input())
arr=[[0]*10 for _ in range(N)]
arr[0] = [1,1,1,1,1,1,1,1,1,1]
i = 1
while i < N:
    for j in range(10):
        for k in range(j,10):
            arr[i][j] += arr[i - 1][k]
    i+=1
print(sum(arr[N-1])%10007)