N=int(input())

arr=[1,1,2]

for i in range(3,N):
    arr.append(arr[i-1]+arr[i-2])

print(arr[N-1])